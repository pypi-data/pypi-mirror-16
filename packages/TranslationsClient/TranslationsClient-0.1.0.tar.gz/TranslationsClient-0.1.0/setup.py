# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="TranslationsClient",
    version="0.1.0",
    description="A translations service Python client",
    long_description=long_description,
    url="https://github.com/GreenelyAB/TranslationsClient",
    author="GreenelyAB",
    author_email="info@greenely.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Communications",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Software Development :: Localization",
        "Topic :: Software Development :: Libraries",
        "Topic :: Text Processing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
    ],
    keywords="translation translations client internationalization",
    packages=find_packages("src", exclude=["tests"]),
    package_dir = {"": "src"},
    install_requires=["pyzmq>=15.2.0"],
    extras_require={
    },
)
