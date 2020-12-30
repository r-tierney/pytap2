#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name="pytap2",
    version="2.1.0",
    description="Object-oriented wrapper around the Linux Tun/Tap device for Python 2 and 3",
    long_description=open("README.rst").read(),
    keywords=("pytap", "tun", "tap", "networking"),
    author="John Hagen",
    author_email="johnthagen@gmail.com",
    url="https://github.com/johnthagen/pytap2",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.6",
    zip_safe=False,
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
