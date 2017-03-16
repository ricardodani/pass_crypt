import argparse
from simplecrypt import encrypt, decrypt

FILE_PATH = 'encpass.txt'

class PassCrypt(object):
    def __init__(self, path):
        self.filepath = path
        if self.has_file():
            self.encrypt_password()
        else:
            self.create_file()

    def has_file(self):
        try:
            self.file_contents = open(self.filepath, 'r')
            return True
        except FileNotFoundError:
            return False

    def encrypt_password(self):
        print('encrypt password')

    def create_file(self):
        print('creating file')

if __name__ == '__main__':
    PassCrypt(FILE_PATH)
