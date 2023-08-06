#!/usr/bin/env python

# Project skeleton maintained at https://github.com/jaraco/skeleton

import io
import sys

import setuptools

with io.open('README.rst', encoding='utf-8') as readme:
	long_description = readme.read()

install_reqs = [
	'cssutils>=0.9.8a3',
	'python-dateutil>=2.0',
	'lxml>=2.0',
	'more_itertools',
	'six',
	'tempora>=1.3',
	'jaraco.itertools',
]

needs_pytest = {'pytest', 'test'}.intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []
needs_sphinx = {'release', 'build_sphinx', 'upload_docs'}.intersection(sys.argv)
sphinx = ['sphinx', 'rst.linker'] if needs_sphinx else []
needs_wheel = {'release', 'bdist_wheel'}.intersection(sys.argv)
wheel = ['wheel'] if needs_wheel else []

name = 'svg.charts'
description = 'Python SVG Charting Library'

setup_params = dict(
	name=name,
	use_scm_version=True,
	author="Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	description=description or name,
	long_description=long_description,
	url="https://github.com/jaraco/" + name,
	packages=setuptools.find_packages(),
	include_package_data=True,
	namespace_packages=name.split('.')[:-1],
	install_requires=install_reqs,
	extras_require={
	},
	setup_requires=[
		'setuptools_scm>=1.9',
	] + pytest_runner + sphinx + wheel,
	tests_require=[
		'pytest>=2.8',
	],
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Intended Audience :: Science/Research",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
	],
	entry_points={
	},
)
if __name__ == '__main__':
	setuptools.setup(**setup_params)
