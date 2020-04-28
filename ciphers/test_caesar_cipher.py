#!/usr/bin/python3
from caesar_cipher import CaesarCipher

def test():
    message = 'The quick brown fox jumped over the lazy dog!. 1234#'
    key = 100
    cipher = CaesarCipher()
    cipher.encryptText(message, key)
    encrypted = cipher.encrypted
    unencrypted = cipher.decryptText(key)
    assert unencrypted == message

def test_brute_force():
    message = 'The quick brown fox jumped over the lazy dog!. 1234#'
    key = 95
    cipher = CaesarCipher()
    cipher.encryptText(message, key)
    encrypted = cipher.encrypted

    for k in range(1, cipher.RNG_CHAR + 1):
        unencrypted = cipher.decryptText(k)
        print(f'Testing key = {k:02d} :', unencrypted)
        if unencrypted == message:
            break
    print(f'Key found after {k} attempts!')
    assert unencrypted == message

if __name__ == '__main__':
    test()
    test_brute_force()