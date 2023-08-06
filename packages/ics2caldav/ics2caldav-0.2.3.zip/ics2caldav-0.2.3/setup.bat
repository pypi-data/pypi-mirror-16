@echo off

setup.py register -r pypi-https
setup.py bdist_wheel upload -r pypi-https
setup.py sdist upload -r pypi-https
