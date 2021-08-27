"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        '''initialize instance of serial generator, starting value at start'''
        self.start = start
        self.next = start-1
    
    def __repr__(self):
        '''string representation of generator'''
        return (f'SerialGenerator start={self.start} next={self.start + 1}')


    def generate(self):
        '''get the next number in the serial'''
        self.next += 1
        return self.next

    def reset(self):
        '''set the serial back to initial start value'''
        self.next = self.start - 1

