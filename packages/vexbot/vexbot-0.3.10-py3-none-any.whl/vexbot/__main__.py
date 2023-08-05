import atexit

from vexbot.commands.start_vexbot import start_vexbot
from vexbot.adapters.shell import main as shell_main


def _kill_vexbot(process):
    def inner():
        process.terminate()

    return inner


def main():
    settings, process = start_vexbot()
    if process and settings.get('kill_on_exit'):
        atexit.register(_kill_vexbot(process))

    shell_settings = settings['shell']
    if process is None:
        already_running = True
    else:
        already_running = False
    shell_settings['--already_running'] = already_running
    for key in set(shell_settings.keys()):
        value = shell_settings.pop(key)
        shell_settings[key[2:]] = value

    # Launch the shell interface
    shell_main(**shell_settings)


if __name__ == "__main__":
    main()
