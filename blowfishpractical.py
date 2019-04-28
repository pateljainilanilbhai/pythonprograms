import blowfish
from os import urandom
key=b"jainilpatel"
print("KEY text value is:",end="")
print(key)
cipher = blowfish.Cipher(key)
print("p value is:",end="")
print(cipher.P)
print("s value is:",end="")
print(cipher.S)
block = b'himyname'
print("plain text value is:",end="")
print(block)
ciphertext = cipher.encrypt_block(block)
print("cipher text value is:",end="")
print(ciphertext)
plaintext = cipher.decrypt_block(ciphertext)
print("decrypted plain text value is:",end="")
print(plaintext)