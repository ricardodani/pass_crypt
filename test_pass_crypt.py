import os
import unittest
from pass_crypt import (
    PassCrypt, NotFoundEncryptedPass, InvalidEncryptionPassword,
    InvalidPassFilename
)

class TestPassCrypt(unittest.TestCase):

    TEST_FILE = 'test.pass'
    TEST_PASSWORD = 'my password'

    def setUp(self):
        self.pc = PassCrypt(self.TEST_FILE)

    def tearDown(self):
        if os.path.isfile(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def test_filename(self):
        self.assertEqual(self.pc.filepath, self.TEST_FILE)

    def test_exception_on_invalid_filename(self):
        with self.assertRaises(InvalidPassFilename):
            PassCrypt('password.txt')

    def test_create_pass_crypt_and_access_it(self):
        self.pc.create_encryption('text to encrypt', self.TEST_PASSWORD)
        with open(self.TEST_FILE, 'rb') as f:
            contents = f.read()
            # test if theres content
            self.assertTrue(len(contents) > 0)
            # test if contents is different from password
            # (meaning that is encrypted)
            self.assertNotEqual(contents, self.TEST_PASSWORD)

        # accessing it
        self.assertEqual(
            self.pc.read_encrypted(self.TEST_PASSWORD),
            b'text to encrypt'
        )

    def test_invalid_password(self):
        self.pc.create_encryption('text to encrypt', self.TEST_PASSWORD)
        with self.assertRaises(InvalidEncryptionPassword):
            self.pc.read_encrypted(self.TEST_PASSWORD + ' wrong')

    def test_invalid_passfile(self):
        pc = PassCrypt('test2.pass')
        with self.assertRaises(NotFoundEncryptedPass):
            pc.read_encrypted('12345')

