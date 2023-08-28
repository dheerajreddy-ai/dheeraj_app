from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in dheeraj_app/__init__.py
from dheeraj_app import __version__ as version

setup(
	name="dheeraj_app",
	version=version,
	description="applicaiton",
	author="dheerraj",
	author_email="dheeraj.k@techbull.co.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
