#!/usr/bin/env python

import os
import sys
import getpass
from simplecrypt import encrypt, decrypt

class NotFoundEncryptedPass(Exception):
    message = 'Not found with the given filename'


class InvalidEncryptionPassword(Exception):
    message = 'Error trying to decrypt, invalid password.'


class InvalidPassFilename(Exception):
    message = 'Invalid Filename (should terminate with .pass)'


class MissingFilenameArgument(Exception):
    message = 'Missing Filename argument.'


class PasswordsDidntMatch(Exception):
    message = 'Passwords don`t match.'


class InvalidTextToEncrypt(Exception):
    message = 'Invalid text to encrypt.'


class NotPossibleToWrite(Exception):
    message = 'The destiny path is not writable or the folder didn`t exists.'


class TooShortPassword(Exception):
    message = 'Password should have at least 6 characters.'


class PassCrypt(object):
    def __init__(self, path):
        if path.endswith('.pass'):
            self.filepath = path
        else:
            raise InvalidPassFilename

    def create_encryption(self, to_encrypt, password):
        try:
            with open(self.filepath, 'wb') as f:
                f.write(encrypt(password, to_encrypt))
        except:
            raise NotPossibleToWrite

    def _decrypt(self, password, contents):
        try:
            return decrypt(password, contents)
        except:
            raise InvalidEncryptionPassword

    def exists(self):
        return os.path.isfile(self.filepath)

    def read_encrypted(self, password):
        if self.exists():
            with open(self.filepath, 'rb') as f:
                decrypted = self._decrypt(password, f.read())
                return decrypted.decode('utf-8')
        raise NotFoundEncryptedPass


class Main(object):

    def __init__(self, *args):
        try:
            self.filename = args[0]
        except:
            raise MissingFilenameArgument
        try:
            self.run()
        except Exception as e:
            print (e.message)


    @staticmethod
    def read_password(confirm=False):
        password = getpass.getpass('Type password: ')
        if len(password) < 6:
            raise TooShortPassword
        if confirm:
            confirm_password = getpass.getpass('Confirm password: ')
            if password != confirm_password:
                raise PasswordsDidntMatch
        return password


    @staticmethod
    def read_contents():
        contents = input('Type text to encrypt:\n')
        if not contents:
            raise InvalidTextToEncrypt
        return contents

    def run(self):
        pc = PassCrypt(self.filename)
        if pc.exists():
            print(
                pc.read_encrypted(self.read_password())
            )
        else:
            pc.create_encryption(
                self.read_contents(),
                self.read_password(confirm=True)
            )
            print ('Done.')


if __name__ == '__main__':
    Main(*sys.argv[1:])
