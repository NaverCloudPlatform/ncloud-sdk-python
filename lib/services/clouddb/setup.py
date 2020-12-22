# coding: utf-8

"""
    clouddb

    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "ncloud-clouddb"
VERSION = "1.1.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="clouddb",
    keywords=["clouddb"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True
)
