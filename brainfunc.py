from functools import partial
import time

class Band:
    def __init__(self, n):
        self.array = [0] * (2*n+1)
        self.middle = n
        self.n = n
        self.pointer = 0

    def _test_out_of_boundaries(self, key):
        if abs(key) > self.n:
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

class Code:
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

class Interpreter:
    def __init__(self, code, n = 10):
        self.band = Band(n)
        self.code = Code(code)
        self.methods = []

    def call_method(self):
        if self.band.get() >= len(self.methods):
            raise Exception(f"Calling function {self.band.get()} while only {len(self.methods)} defined!")
        method_code = Code(self.methods[self.band.get()])
        self._execute(method_code)

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

    def _execute(self, code):
        brackets = []
        mappings = {
            '>': self.band.move_right,
            '<': self.band.move_left,
            '+': self.band.inc,
            '-': self.band.dec,
            '[': partial(self.loop_open, code, brackets),
            ']': partial(self.loop_close, code, brackets),
            '(': self.define_method,
            '*': self.call_method,
        }
        while not code.eof():
            command = code.get()
            if command in mappings.keys():
                print(command)
                self.band.visualize()
                mappings[command]()
                code.next()

    def run(self):
        self._execute(self.code)

if __name__ == '__main__':
    code = "(>-<+<+<+<++*[<+++*>+*>>>+<<<++*])" + \
    "(->>[-<<+>>]<[->+<<+>]<[->+<])" + \
    "(-->>>>[-<<<<+<+>>>>>]<<<<<[->>>>>+<<<<<]>>>>[-<<<-<+>>>>]<<<<[->>>>+<<<<]>)" + \
    "(--->[-]<)" + \
    "+++++++++++++++<*" # Fibonacci(15)
    interpreter = Interpreter(code)
    interpreter.run()