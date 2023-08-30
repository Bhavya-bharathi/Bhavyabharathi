from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in bhavya_app/__init__.py
from bhavya_app import __version__ as version

setup(
	name="bhavya_app",
	version=version,
	description="system",
	author="bhavya",
	author_email="bhavya2akkala@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
