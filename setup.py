from setuptools import setup

setup(
    name="ZimPhoneValidate",
    version="1.1.5",
    author="Tanaka Chinengundu",
    author_email="tanakah30@gmail.com",
    long_description="""
	**Easy-to-use Zimbabwean Mobile Number Validation**

This module provides a simple and convenient way to validate Zimbabwean mobile phone
numbers. It supports all major mobile network operators in Zimbabwe, including:

* Econet
* NetOne
* Telecel

**Key features:**

* Simple API: Validate phone numbers with just one line of code.
* Extensive coverage: Supports all major mobile network operators in Zimbabwe.
* Fast and reliable: Validations are performed quickly and accurately.
* Lightweight: The module has a small footprint and minimal dependencies.

**Installation:**

::

    pip install ZimPhoneValidate

**Usage:**

::

    from ZimPhoneValidate.validate import number_is_valid

    number = "263771234567"


    if number_is_valid(number):
        print(f"{number} is a valid Zimbabwean mobile number.")
    else:
        print(f"{number} is not a valid Zimbabwean mobile number.")

**Applications:**

This module can be useful for applications such as:

* Contact management systems
* User registration forms
* SMS marketing campaigns
* Mobile payment systems

**Note:**

This module is under development. Feel free to contribute to the project by reporting
bugs or suggesting improvements.

	""",
    license="MIT",
    url="https://github.com/taqsblaze/ZimPhoneValidate",
    install_requires=["pip"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    entry_points={
        "console_scripts": [
            "example=ZimPhoneValidate.validate:example.show"
        ]
    },
)
