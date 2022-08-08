class Band:
    """
    The Band class implements the band functionality
    like the commands "+", "-", ">", "<". The band
    pointer starts at position 0 and its allowed positions
    are everywhere between and including (-n) and (+n)

    :param n: The length of the band will be 2n+1 centered
        around the position 0.
    """
    def __init__(self, n):
        self.array = [0] * (2*n+1)
        self.middle = n
        self.pointer = 0

    def _test_out_of_boundaries(self, key):
        if abs(key) > self.middle:
            raise Exception("Index out of the band's boundaries!")

    def __setitem__(self, key, value):
        self._test_out_of_boundaries(key)
        self.array[self.middle + key] = value

    def __getitem__(self, key):
        self._test_out_of_boundaries(key)
        return self.array[self.middle + key]

    def get(self):
        return self[self.pointer]

    def inc(self):
        # TODO: Make it work like a byte
        self[self.pointer] += 1

    def dec(self):
        # TODO: Make it work like a byte
        self[self.pointer] -= 1

    def move_right(self):
        self.pointer += 1
        self._test_out_of_boundaries(self.pointer)

    def move_left(self):
        self.pointer -= 1
        self._test_out_of_boundaries(self.pointer)

    def visualize(self):
        print(self.array)
        print((1 + (self.middle + self.pointer) * 3) * ' ' + '*')