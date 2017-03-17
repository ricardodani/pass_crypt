# pass_crypt
pass_crypt.py, or just pass_crypt, is a tool for encrypt passwords in .pass files.

It uses 'pycrypto' to encrypt, save, decrypt and display passwords, but you can use it for another purposes, of course.


## Development

### To install

    $ git clone git@github.com:ricardodani/pass_crypt && cd pass_crypt
    $ pip install -r requirements.txt

### To test

    $ py.test

### Tested on

- Python 3.6.0


## Using

### To create a new password vault (the vaulted file should end with .pass)

    $ ./pass_crypt.py name-of-my-encrypted-file.pass

```
Type text to encrypt:
My text of test
Type password:
Confirm password:
Done.
```
 
### To read a vaulted file, use the same command after the creation

    $ ./pass_crypt.py name-of-my-encrypted-file.pass

```
Type password:
My text of test
```
