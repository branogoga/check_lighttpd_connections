import hello

import unittest

class   TestHello(unittest.TestCase):

    def testSay(self):
        self.assertEqual(hello.say("Hello world"), "Hello world")
        self.assertEqual(hello.say("test"), "test")