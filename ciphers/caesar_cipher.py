#!/usr/bin/python3

class CaesarCipher():
    """ Class implementation of Caesar Cipher """
    #   ASCII Reference
    #   ' '     32
    #   [A-Z]   65 - 90 
    #   [a-z]   97 - 112    
    #   [0-9]   48 - 57
    #   ~       126
    MIN_CHAR = 32   # [space] 
    MAX_CHAR = 126  # [tilde] ~
    RNG_CHAR = 126 - 32 + 1

    def __init__(self):
        pass

    def __run_cipher(self, message: str, key: int = 0) -> str:
        return ''.join([chr((ord(m) + key - CaesarCipher.MIN_CHAR) % CaesarCipher.RNG_CHAR + CaesarCipher.MIN_CHAR) for m in message])

    def encryptText(self, text: str, key: int=0) -> None:
        self.encrypted = self.__run_cipher(text, key)

    def decryptText(self, key: int) -> str:
        return self.__run_cipher( self.encrypted, -key)

if __name__ == '__main__':
    message = 'The quick brown fox jumped over the lazy dog!. 1234#'
    key = 2
    cc = CaesarCipher()
    cc.encryptText(message, key)
    encrypted = cc.encrypted
    print('Encrypted message:', encrypted)
    unencrypted = cc.decryptText(key)
    print('Unencrypted message:', unencrypted)
    assert unencrypted == message