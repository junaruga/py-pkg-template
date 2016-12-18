import pytest
from unittest.mock import MagicMock

from foobar.application import Application


def test_init():
    app = Application()
    assert app


def test_parse_argv_no_options():
    app = Application()
    args = app.parse_argv(['prog', 'arg1_value'])
    assert args
    assert args.arg1 == 'arg1_value'
    assert args.something == 'foo'


def test_parse_argv_something():
    app = Application()
    args = app.parse_argv(['prog', 'arg1_value', '-s', 'bar'])
    assert args
    assert args.arg1 == 'arg1_value'
    assert args.something == 'bar'


def test_do_foo_error():
    app = Application()

    app.do_foo = MagicMock(return_value=False)
    with pytest.raises(ValueError):
        app.do_bar()
