import argparse
import logging

import foobar

LOG = logging.getLogger(__name__)


class Application(object):
    """An application class."""

    def __init__(self):
        self._program = 'command-a'
        self._version = foobar.__version__

    def run(self, argv=None):
        LOG.info("Starting %s (%s)", self._program, self._version)
        is_error = False
        try:
            self.run_internally(argv)
        except KeyboardInterrupt as e:
            print('... stopped')
            LOG.error('Caught keyboard interrupt from user')
            LOG.exception(e)
            is_error = True

        raise SystemExit(is_error)

    def run_internally(self, argv):
        args = self.parse_argv(argv)
        print('args: {0}'.format(args))
        return True

    def parse_argv(self, argv=None):
        args = None
        if argv:
            args = argv[1:]
        parser = argparse.ArgumentParser()
        parser.add_argument('arg1')
        parser.add_argument('-s', '--something', default='foo')
        parsed_args = parser.parse_args(args)
        return parsed_args

    def do_foo(self):
        return True

    def do_bar(self):
        if not self.do_foo():
            raise ValueError('Foo is invalid')
        return True
