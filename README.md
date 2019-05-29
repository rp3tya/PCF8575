PCF8575
=======

Python library for the PCF8575 I2C IO expander. It abstracts the 16 bit IO port as a Python list, and allows the read/writing of individual pins or the whole port at once.
This is a modified version of the [PCF8574](https://github.com/flyte/pcf8574) library to support the extra 8 ports.

## Installation

The library depends on the `smbus-cffi` package. You may need to `apt-get install libffi-dev` if you're on a debian based system. Otherwise, simply:

```
pip install pcf8575
```

## Usage

```python
In [1]: from pcf8575 import PCF8575

In [2]: i2c_port_num = 1

In [3]: pcf_address = 0x20

In [4]: pcf = PCF8575(i2c_port_num, pcf_address)

In [5]: pcf.port
Out[5]: [True, True, True, True, True, True, True, True]

In [6]: pcf.port[0] = False

In [7]: pcf.port
Out[7]: [False, True, True, True, True, True, True, True]

In [8]: pcf.port = [True, False, True, False, True, False, True, False]

In [9]: pcf.port
Out[9]: [True, False, True, False, True, False, True, False]

In [10]: pcf.port[7]
Out[10]: False

In [11]: pcf.port[6]
Out[11]: True
```
