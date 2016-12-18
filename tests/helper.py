import os
import shutil
import tempfile


def touch(path):
    with open(path, 'a'):
        os.utime(path, None)


def do_with_working_dir():
    working_dir = None
    try:
        working_dir = tempfile.mkdtemp(prefix='foo-bar-test-')
        yield working_dir
    finally:
        if os.path.isdir(working_dir):
            shutil.rmtree(working_dir)
