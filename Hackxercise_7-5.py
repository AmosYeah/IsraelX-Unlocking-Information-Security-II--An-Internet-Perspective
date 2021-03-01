# Hackxercise_7-5

# Real RSA system:
# Use pycrypto to sign and verify a message using RSA.

from Crypto.PublicKey import RSA

key = RSA.generate(2048)

private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')

def sign(m, private_key):
    return key.decrypt(m)

def verify(m, s, public_key):
    if key.encrypt(s, public_key) == m:
        return True
    else:
        return False
        
#  test
print(sign(3, private_key))

print(verify(3, sign(3, private_key), public_key))
