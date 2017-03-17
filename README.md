# py-simple-vault
A python script tool for vault passwords based on simple-crypto's library

## Installing

    pip install -r requirements.txt

## Using

### To create a new password vault (the vaulted file should end with .pass)

    $ ./pass_crypt.py name-of-my-encrypted-file.pass

- It will ask for the content you want to encrypts, and the password (with confirmation) you want to encrypt it with:

    ```
    Type text to encrypt:
    
    My text of test
    
    Type password: 123
    
    Confirm password: 123
    
    Done.
    ```
    
### To read a vaulted file, use the same command after create it

    $ ./pass_crypt.py name-of-my-encrypted-file.pass

- It will ask for the password and return the decrypted content:

    ```
    Type password: 123
    My text of test
    ```
    
- Simple, huhn?
