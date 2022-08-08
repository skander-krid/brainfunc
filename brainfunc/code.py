class Code:
    """
    The Code class holds the source code for the brainfunc 
    program, while managing an instruction pointer.
    """
    def __init__(self, code):
        self.code = code
        self.pointer = 0

    def next(self):
        self.pointer += 1

    def eof(self):
        return self.pointer >= len(self.code)

    def jump(self, to):
        self.pointer = to

    def get(self):
        return self.code[self.pointer]