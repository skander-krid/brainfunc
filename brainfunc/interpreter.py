from functools import partial
from brainfunc.band import Band
from brainfunc.code import Code

class Interpreter:
    """
    An interpreter takes the brainfunc code as input to
    run it when the run() function is called.

    :param code: The brainfunc code.
    :type code: string

    :param n: (Optional) The length of the band will be (2n+1).
    :type n: int
    """
    #TODO: Find better design for this class
    def __init__(self, code, n = 10):
        self.band = Band(n)
        self.code = Code(code)
        self.methods = []

    def call_method(self, verbose):
        if self.band.get() >= len(self.methods):
            raise Exception(f"Calling function {self.band.get()} while only {len(self.methods)} defined!")
        method_code = Code(self.methods[self.band.get()])
        self._execute(method_code, verbose)

    def define_method(self):
        self.code.next()
        method = ''
        while not self.code.eof() and self.code.get() != ')':
            if self.code.get() == '(':
                raise Exception("Nested method definitions not allowed!")
            method += self.code.get()
            self.code.next()
        self.methods.append(method)

    def loop_open(self, code, brackets):
        if len(brackets) == 0 or brackets[-1] != code.pointer:
            # first visit in this opening bracket
            brackets.append(code.pointer)

        if self.band.get() == 0:
            while not code.eof() and code.get() != ']':
                code.next()
            brackets.pop(-1)

    def loop_close(self, code, brackets):
        if self.band.get() != 0:
            code.jump(brackets[-1])
        else:
            brackets.pop(-1)

    def _execute(self, code, verbose):
        # TODO: Find a better way to decompose this function
        brackets = []
        mappings = {
            '>': self.band.move_right,
            '<': self.band.move_left,
            '+': self.band.inc,
            '-': self.band.dec,
            '[': partial(self.loop_open, code, brackets),
            ']': partial(self.loop_close, code, brackets),
            '(': self.define_method,
            '*': partial(self.call_method, verbose),
        }
        while not code.eof():
            command = code.get()
            if command in mappings.keys():
                if verbose:
                    self.band.visualize()
                    print(command)
                mappings[command]()
                code.next()

    def run(self, verbose=True):
        self._execute(self.code, verbose=verbose)
        if verbose:
            self.band.visualize()

if __name__ == '__main__':
    code = "(>[->+<]>)+++<+++++++<*"
    interpreter = Interpreter(code)
    interpreter.run()