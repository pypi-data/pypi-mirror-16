import codecs

from os import path
from setuptools import find_packages, setup


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()


setup(
    author="Pinax Team",
    author_email="developers@pinaxproject.com",
    description="an event logger for Django projects",
    name="pinax-eventlog",
    long_description=read("README.rst"),
    version="1.1.2",
    url="http://pinax-eventlog.rtfd.org/",
    license="MIT",
    packages=find_packages(),
    test_suite="runtests.runtests",
    install_requires=[
        "jsonfield>=1.0.3"
    ],
    tests_require=[
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
