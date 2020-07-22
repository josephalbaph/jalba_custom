# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in jalba_custom/__init__.py
from jalba_custom import __version__ as version

setup(
	name='jalba_custom',
	version=version,
	description='Customizations by Joseph Alba',
	author='Joseph Marie Alba',
	author_email='josephalbaph@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
