# coding: utf-8

"""
    sdk

    OpenAPI spec version: 2018-06-21T02:27:10Z

"""

import io
from setuptools import setup, find_packages  # noqa: H301

NAME = "ncloud-sdk"
VERSION = "1.0.6"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15"
            , "six >= 1.10"
            , "certifi"
            , "python-dateutil"
            , "ncloud-apikey >= 1.0.5"
            , "ncloud-server >= 1.0.5"
            , "ncloud-loadbalancer >= 1.0.5"
            , "ncloud-autoscaling >= 1.0.5"
            , "ncloud-monitoring >= 1.0.5"
            , "ncloud-cdn >= 1.0.5"
            , "ncloud-clouddb >= 1.0.5"]

with io.open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description="ncloud-sdk",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=["ncloud-sdk", "ncloud"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True
)
