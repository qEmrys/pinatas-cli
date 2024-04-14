from setuptools import setup, find_packages
from os.path import join, dirname
import src

setup(
    name = 'pinatas',
    version = src.__version__,
    packages = find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    entry_points = {
        'console_scripts': [
            'pinatas = src.__main__:main'
        ]
    })
