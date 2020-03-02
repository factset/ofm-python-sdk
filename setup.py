# coding: utf-8

"""
    Open:FactSet Marketplace API

    Headless CMS API used by the Open:FactSet Marketplace.  # noqa: E501

    OpenAPI spec version: v2.1.5
    Contact: openfactset-frontend-engineering@factset.com
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "ofm-client"
VERSION = "1.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="Open:FactSet Marketplace API",
    author_email="openfactset-frontend-engineering@factset.com",
    url="",
    keywords=["ofm", "Open:FactSet Marketplace API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Headless CMS API used by the Open:FactSet Marketplace.  # noqa: E501
    """
)
