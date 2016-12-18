import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
import foobar  # noqa: E402

setup(
    name='foobar',
    license='Public Domain',
    version=foobar.__version__,
    description='Foo bar that is Python package template.',
    author='Your Name',
    author_email='your_emal@example.com',
    url='https://github.com/junaruga/py-pkg-template',
    package_dir={'': 'lib'},
    packages=[
        'foobar',
        'foobar.main',
    ],
    entry_points={
        'console_scripts': [
            'command-a=foobar.main.commanda:main',
        ]
    },
    setup_requires=[],
    classifiers=[
        # TODO(Add items)
    ],
)
