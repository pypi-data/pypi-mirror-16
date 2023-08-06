from setuptools import setup

setup(
    name = 'pyagram',
    version = '1.0.1',
    description = 'Pyagram: Python Finite State Machine Diagram Generator',
    author = 'Hideshi Ogoshi',
    author_email = 'hideshi.ogoshi@gmail.com',
    url = 'https://github.com/hideshi',
    packages = ['pyagram'],
    install_requires=[
        'pyparsing',
    ],
)
