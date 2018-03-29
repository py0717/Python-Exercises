# Hello World

import unittest


class hello_world:
    def hello():
        """ returns the string 'Hello, World!' """
        return('Hello, World!')

# test from exercism
class HelloWorldTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_world.hello(), 'Hello, World!')

# run test
unittest.main()        
