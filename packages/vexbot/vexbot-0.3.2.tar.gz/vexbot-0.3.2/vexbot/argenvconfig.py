import argparse as _argparse
import yaml as _yaml
from os import getenv as _getenv


class ArgEnvConfig:
    def __init__(self):
        self._environ = {}
        self._arg = _argparse.ArgumentParser()

    def initialize_argparse(self,
                            prog=None,
                            usage=None,
                            description=None,
                            epilog=None,
                            parents=[],
                            formatter_class=_argparse.HelpFormatter,
                            prefix_chars='-',
                            fromfile_prefix_chars=None,
                            argument_default=None,
                            conflict_handler='error',
                            add_help=True,
                            allow_abbrev=True):

        self._arg = _argparse.ArgumentParser(prog,
                                             usage,
                                             description,
                                             epilog,
                                             parents,
                                             formatter_class,
                                             prefix_chars,
                                             fromfile_prefix_chars,
                                             argument_default,
                                             conflict_handler,
                                             add_help,
                                             allow_abbrev)


    def add_argument(self, *args, **kwargs):
        try:
            environ = kwargs.pop('environ')
        except KeyError:
            environ = None

        argument = self._arg.add_argument(*args, **kwargs)

        if environ:
            self._environ[argument.dest] = environ

    def add_environment_variable(self, *args, **kwargs):
        pass

    def add_settings_file(self, *args, **kwargs):
        pass

    def get(self, value):
        args = self._arg.parse_args()
        result = getattr(args, value)
        if result is None:
            key = self._environ.get(value)
            if key:
                result = _getenv(key)
            else:
                result = None
        return result

    def get_args(self):
        return self._arg.parse_args()

    def load_settings(self, filepath):
        with open(filepath) as f:
            settings = _yaml.load(f)
        return settings
        settings = _yaml.load(filepath)
