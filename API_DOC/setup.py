# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Tweet Master API",
    author_email="calongefederico@gmail.com",
    url="",
    keywords=["Swagger", "Tweet Master API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    API que permite extraer informacion de Twitter. Mediante esta API se pueden generar campañas de extracción de información de TWitter, que se ejecuten cada cierto tiempo. Y en base a esa información se generan reportes.
    """
)

