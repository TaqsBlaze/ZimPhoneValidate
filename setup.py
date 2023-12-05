#!/usr/bin/env python
from setuptools import setup

setup(
    name="ZimPhoneValidate",
    version="1.0.0",
    author="Tanaka Chinengundu",
    author_email="tanakah30@gmail.com",
    long_description="A package for easily validating Zimbabwean phone numbers in your python applications",
    license="MIT",
    url="https://wa.me/263778040497?text=More+details+about+ZimPhoneValidate+package",
    install_requires=["pip"],
    classifiers=["regex","phone number","verify"],
    examples_location = "example/*",
    entry_points={"cli":["ZimPhoneValidate=validate","cli=validate.isvalid"]}
)
