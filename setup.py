import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pcf8575",
    version="0.3",
    author="rp3tya",
    author_email="rpetya@hotmail.com",
    description="Library for communication with PCF8575 IO expander over I2C",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rp3tya/PCF8575",
    install_requires=['smbus-cffi'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="pcf8575 pcf8574 i2c i/o expander multiplexer",
)

