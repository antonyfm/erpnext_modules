from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in fme/__init__.py
from fme import __version__ as version

setup(
	name="fme",
	version=version,
	description="FME Modules",
	author="FME",
	author_email="antony@fmeuae.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
