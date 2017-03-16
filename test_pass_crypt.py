import unittest
from pass_crypt import PassCrypt

class TestPassCrypt(unittest.UnitTest):

    def test_create_pass_crypt(self):
        pc = PassCrypt('test.pass')
        pc.create_encryption('text to encrypt', 'my password')
        with open('test.pass', 'r') as f:
            self.assertTrue(len(f.read()) > 0)
