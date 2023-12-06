from setuptools import setup

setup(
    name="ZimPhoneValidate",
    version="1.1.0",
    author="Tanaka Chinengundu",
    author_email="tanakah30@gmail.com",
    long_description="A package for easily validating Zimbabwean phone numbers in your Python applications",
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
