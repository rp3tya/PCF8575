import smbus

class IOPort(list):
    """
    Represents the PCF8575 IO port as a list of boolean values.
    """
    def __init__(self, pcf8575, *args, **kwargs):
        super(IOPort, self).__init__(*args, **kwargs)
        self.pcf8575 = pcf8575

    def __setitem__(self, key, value):
        """
        Set an individual output pin.
        """
        self.pcf8575.set_output(key, value)

    def __getitem__(self, key):
        """
        Get an individual pin state.
        """
        return self.pcf8575.get_pin_state(key)

    def __repr__(self):
        """
        Represent port as a list of booleans.
        """
        state = self.pcf8575.bus.read_word_data(self.pcf8575.address, 0)
        ret = []
        for i in range(16):
            ret.append(bool(state & 1<<15-i))
        return repr(ret)

    def __len__(self):
        return 16

    def __iter__(self):
        for i in range(16):
            yield self[i]

    def __reversed__(self):
        for i in range(16):
            yield self[15-i]


class PCF8575(object):
    """
    A software representation of a single PCF8575 IO expander chip.
    """
    def __init__(self, i2c_bus_no, address):
        self.bus_no = i2c_bus_no
        self.bus = smbus.SMBus(i2c_bus_no)
        self.address = address

    def __repr__(self):
        return "PCF8575(i2c_bus_no=%r, address=0x%02x)" % (self.bus_no, self.address)

    @property
    def port(self):
        """
        Represent IO port as a list of boolean values.
        """
        return IOPort(self)

    @port.setter
    def port(self, value):
        """
        Set the whole port using a list.
        """
        assert isinstance(value, list)
        assert len(value) == 16
        new_state = 0
        for i, val in enumerate(value):
            if val:
                new_state |= 1 << 15-i
        self.bus.write_byte_data(self.address, new_state & 0xff, (new_state >> 8) & 0xff)

    def set_output(self, output_number, value):
        """
        Set a specific output high (True) or low (False).
        """
        assert output_number in range(16), "Output number must be an integer between 0 and 15"
        current_state = self.bus.read_word_data(self.address, 0)
        bit = 1 << 15-output_number
        new_state = current_state | bit if value else current_state & (~bit & 0xffff)
        self.bus.write_byte_data(self.address, new_state & 0xff, (new_state >> 8) & 0xff)

    def get_pin_state(self, pin_number):
        """
        Get the boolean state of an individual pin.
        """
        assert pin_number in range(16), "Pin number must be an integer between 0 and 15"
        state = self.bus.read_word_data(self.address, 0)
        return bool(state & 1<<15-pin_number)

