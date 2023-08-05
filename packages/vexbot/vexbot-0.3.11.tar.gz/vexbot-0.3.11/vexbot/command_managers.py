import logging # flake8: noqa
import collections as _collections

from vexmessage import Message as VexMessage

from vexbot.commands.restart_bot import restart_bot as _restart_bot
from vexbot.function_wrapers import (msg_list_wrapper,
                                     no_arguments)


class CommandManager:
    def __init__(self, messaging):
        # NOTE: commands is a dict of dicts and there is nested parsing
        self._commands = {}
        self._messaging = messaging
        self._commands['help'] = msg_list_wrapper(self._help)
        self._commands['commands'] = self._cmd_commands

    def register_command(self,
                         command: str,
                         function_or_dict: (_collections.Callable, dict)):
        """
        `func_or_nested` can either be a function or a dictionary
        """
        self._commands[command] = function_or_dict

    def is_command(self,
                   command: str,
                   call_command: bool=False) -> bool:

        callback, command, args = self._get_callback_recursively(command)
        if callback and call_command:
            callback(args)
            return True
        else:
            return bool(callback)

    def parse_commands(self, msg: VexMessage):
        command = msg.contents.get('command')

        if not command:
            return

        args = msg.contents.get('args')

        callback, command, args = self._get_callback_recursively(command, args)
        msg.contents['parsed_args'] = args

        if callback:
            results = callback(msg)
            # logging.error('{} {}'.format(results, command))

            if results:
                self._messaging.send_response(target=msg.source,
                                              original=command,
                                              response=results)

    def _get_callback_recursively(self,
                                  command: str,
                                  args: (list,
                                         str)=None) -> (_collections.Callable,
                                                        str,
                                                        list):
        """
        returns callback, command string, and args
        """

        if not command:
            return None, None, None
        if isinstance(args, str):
            args = args.split()
        elif args is None:
            args = []

        callback = self._commands.get(command)

        if isinstance(callback, _collections.Callable):
            return callback, command, args
        elif isinstance(callback, dict):
            dict_ = callback
        elif callback is None:
            return None, None, None
        else:
            s = '{} is not a callable function or a dict'
            raise TypeError(s.format(command))

        if not args:
            return None, None, None
        commands = []
        commands.append(command)

        # NOTE: Can't iterate None
        for command_number, command in enumerate(args):
            callback = dict_.get(command)
            if callback is None:
                return None, None, None

            commands.append(command)
            # dynamically reassigns the `dict_` value to travese nested dicts
            if isinstance(callback, dict):
                dict_ = callback
            elif isinstance(callback, _collections.Callable):
                break
            else:
                s = '{} is not a callable function or a dict'
                raise TypeError(s.format(callback.__name__))

        command_number += 1

        command_str = ' '.join(commands)
        return callback, command_str, args[command_number:]

    def _cmd_commands(self, msg: VexMessage):
        """
        returns a list of all available commands
        works recursively
        """
        def get_commands(d: dict):
            """
            recursive command
            """
            commands = []
            if not isinstance(d, dict):
                return commands

            for k, v in d.items():
                if isinstance(v, dict):
                    # NOTE: recursive command
                    stuff = get_commands(v)
                    for s in stuff:
                        commands.append(k + ' ' + s)
                else:
                    commands.append(k)
            return commands

        return get_commands(self._commands)

    def _send_command_not_found(self, target: str, original: str):
        """
        helper method
        """
        self._messaging.send_response(target=target,
                                      response='Command not found',
                                      original=original)

    def _help(self, args=None):
        if not args:
            return self._commands.keys()
        else:
            docs = []
            for arg in args:
                doc = self._commands.get(arg, None).__doc__
                if doc:
                    docs.append(doc)

            if docs:
                return docs


class BotCommandManager(CommandManager):
    def __init__(self, robot):
        super().__init__(robot.messaging)
        # nested command dict
        subprocess = {}

        # alias for pep8
        s_manager = robot.subprocess_manager

        # Store a reference to the subprocess settings for the `alive` command
        self._subprocess_settings = s_manager._settings
        subprocess['settings'] = msg_list_wrapper(s_manager.get_settings, 1)
        # subprocess['set-settings'] = msg_unpack_args(s_manager.update, 3)

        self._commands['subprocess'] = subprocess

        self._commands['killall'] = no_arguments(s_manager.killall)
        self._commands['restart_bot'] = no_arguments(_restart_bot)
        self._commands['alive'] = self._alive

        self._commands['start'] = msg_list_wrapper(s_manager.start)
        registered = s_manager.registered_subprocesses
        self._commands['subprocesses'] = no_arguments(registered)
        self._commands['restart'] = msg_list_wrapper(s_manager.restart)
        self._commands['kill'] = msg_list_wrapper(s_manager.kill)
        self._commands['terminate'] = msg_list_wrapper(s_manager.terminate)
        running = s_manager.running_subprocesses
        self._commands['running'] = no_arguments(running)

    def _alive(self, msg):
        """
        queries the subprocesses to check their status using messaging.

        can also use the `running` command to see what's running locally
        """
        # FIXME
        values = list(self._commands['subprocesses'](msg))

        process_names = []
        for value in values:
            setting = self._subprocess_settings.get(value)
            process_name = None
            if setting:
                if setting.get('--service_name'):
                    process_name = setting['--service_name']
            if process_name is None:
                process_name = value
            process_names.append(process_name)
        if process_names:
            try:
                process_names.remove(msg.source)
            except ValueError:
                pass
            for process_name in process_names:
                self._messaging.send_command(target=process_name,
                                             command='alive')


class AdapterCommandManager(CommandManager):
    def __init__(self, messaging):
        super().__init__(messaging)
        self._commands['alive'] = no_arguments(self._alive)

    def _alive(self, *args):
        self._messaging.send_status('CONNECTED')
