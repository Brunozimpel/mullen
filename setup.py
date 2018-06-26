from setuptools import setup, find_packages

# Model package name
NAME = 'Mullen'

# Default package dir
PKG_DIR = 'mullen'

# Current Version
VERSION = {}
with open("%s/version.py" % PKG_DIR) as fp:
    exec(fp.read(), VERSION)

DEPENDENCIES = [
   'fire',
   'numpy',
   'tensorflow',
   'keras',
   'opencv'
]

setup(
    name=NAME,
    version=VERSION['__version__'],
    description='Mullen the skate trick classifier',
    author='Matheus Frata',
    author_email='matheus.frata@gmail.com',
    packages=find_packages(exclude=("tests",)),
    install_requires=DEPENDENCIES, #external packages as dependencies
)

