# Hackxercise_7-3

# A real RSA system:
# Use pycrypto to encrypt and decrypt a message using RSA.

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes

key = RSA.generate(2048)

private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')

def encrypt(m, public_key):
    return key.encrypt(m, public_key)
    # return ciphertext and key

def decrypt(c, private_key):
    return key.decrypt(c)
    # TODO

# Test encrypt and decrypt
cipher = encrypt(3, public_key)
print(cipher[0])
print(decrypt(cipher[0], private_key))