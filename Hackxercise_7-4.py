# Hackxercise_7-4

# Toy RSA system:
# Implement the function sign, which receives a number and a private key and returns a signature of it; and the function verify, which receives a number with a signature and the public key, and returns whether the signature is valid.

n = 33
e = 7
d = 3
public_key = (n, e)
private_key = (n, d)

def sign(m, private_key):
    return (m ** private_key[1]) % private_key[0]

def verify(m, s, public_key):
    if (s ** public_key[1]) % public_key[0] == m:
        return 1 # true
    else:
        return 0 # false
        
#  test
print(sign(3, private_key))

print(verify(3, sign(3, private_key), public_key))
