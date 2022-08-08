from brainfunc import Interpreter
import unittest

class InterpreterTestCase(unittest.TestCase):
    def test_fibonacci(self):
        """
        Test the interpreter through a brainfunc function which
        computes the fibonacci sequence.
        
        The implementation uses the DP approach, but the time complexity
        is still exponential. To understand why, remember that the
        Fibonacci sequence is bounded between two exponential functions,
        which makes it asymptotically equivalent to an exponential function.
        Now let's consider a brainfuck sequence that copies the value of
        fib(n) from band position x to (x-1).
        The brainfunc code for that will look sth like this: [-<+>]<
        Obviously the computation time is linear for input size fib(n)
        and therefore exponential for input size n.
        """

        def fib(n):
            lo, hi = 0, 1
            counter = 0
            while counter != n:
                lo, hi = hi, lo + hi
                counter += 1
            return lo

        # TODO: Tests/ fix this code for n = 0, 1, 2
        # TODO: Fix the function 0 so that the garbage is
        #       is deleted and only the result remains after
        #       the function returns
        code = "(>-<+<+<+<++*[<+++*>+*>>>+<<<++*])" + \
        "(->>[-<<+>>]<[->+<<+>]<[->+<])" + \
        "(-->>>>[-<<<<+<+>>>>>]<<<<<[->>>>>+<<<<<]>>>>[-<<<-<+>>>>]<<<<[->>>>+<<<<]>)" + \
        "(--->[-]<)" + \
        "+++++++++++++++<*"
        interpreter = Interpreter(code)
        interpreter.run(verbose=False)
        interpreter.band.move_right()
        self.assertEqual(interpreter.band.get(), fib(15))
    
    def test_addition(self):
        code = "(>[->+<]>)+++<+++++++<*"
        interpreter = Interpreter(code)
        interpreter.run(verbose=False)
        self.assertEqual(interpreter.band.get(), 10)