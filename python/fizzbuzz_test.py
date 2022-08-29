import unittest
from fizzbuzz import fizzbuzz

# https: // www.devdungeon.com/content/python-use-stringio-capture-stdout-and-stderr
from io import StringIO  # Python 3
import sys

# Create the in-memory "file"
temp_out = StringIO()

# Replace default stdout (terminal) with our stream
sys.stdout = temp_out

print('8')
print('Fizz')
print('Buzz')
print('11')
print('Fizz')
print('13')
print('14')
print('FizzBuzz')
print('16')
print('17')
print('Fizz')
print('19')
print('Buzz')

# The original `sys.stdout` is kept in a special
# dunder named `sys.__stdout__`. So you can restore
# the original output stream to the terminal.
sys.stdout = sys.__stdout__

# sys.stdout.write(temp_out.getvalue())


class FizzBuzzTest(unittest.TestCase):
    def test_8_to_17(self):
        self.assertEqual(fizzbuzz(8, 17),
                         None)
        #self.assertEqual(sys.stdout, temp_out)
        print(sys.__stdout__.flush())
        print('+++++++')
        print(temp_out.flush())


if __name__ == "__main__":
    unittest.main()
