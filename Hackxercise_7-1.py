# Hackxercise_7-1

# Implement a toy Diffie-Hellman system by completing the Diffie-Hellman key exchange protocol:
# supply the “publish” and “compute_secret” methods for both Alice and Bob.

# Alice's publish() should return the message to be sent to Bob
# Bob's publish() should return the message to be sent to Alice
# Both their compute_secret() should, given the message from the other party, return the agreed-upon secret

import random

p = 283
g = 47

class Alice:

    def __init__(self):
        self.a = random.randint(1, p)

    def publish(self):
        return g ** self.a % p

    def compute_secret(self, gb):
        return gb ** self.a % p

class Bob:

    def __init__(self):
        self.b = random.randint(1, p)

    def publish(self):
        return g ** self.b % p

    def compute_secret(self, ga):
        return ga ** self.b % p

alice = Alice()
bob = Bob()
print('Alice selected: %s' % alice.a)
print('Bob selected: %s' % bob.b)
ga = alice.publish()
gb = bob.publish()
print('Alice published: %s' % ga)
print('Bob published: %s' % gb)
sa = alice.compute_secret(gb)
sb = bob.compute_secret(ga)
print('Alice computed: %s' % sa)
print('Bob computed: %s' % sb)