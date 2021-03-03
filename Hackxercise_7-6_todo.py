# Hackxercise_7-6

# Implement the function weak-HMAC, which receives message and a  8 -bytes ( 64 -bit) long key, and returns its HMAC using SHA-1 with the given  8 -byte ( 64 -bit) ipad and opad.

# TODO:
# Your solution was successfully submitted.
# You passed 0% of all tests.

from hashlib import sha1

ipad = b'123455678'
opad = b'abcdefghi'

def bitwise_xor_bytes(a, b):
    result_int = int.from_bytes(a, byteorder="big") ^ int.from_bytes(b, byteorder="big")
    return result_int.to_bytes(max(len(a), len(b)), byteorder="big")

def weak_hmac(m, k, ipad, opad):
    
    m = bytes(m, 'UTF-8')
    k = bytes(k, 'UTF-8')
    s1 = sha1()
    data1 = bitwise_xor_bytes(ipad, k) + m
    s1.update(data1)
    h1 = s1.hexdigest()
    
    h1 = bytes(h1, 'UTF-8')
    s2 = sha1()
    data2 = bitwise_xor_bytes(opad, k) + h1
    s2.update(data2)
    h2 = s2.hexdigest()
    
# Test
weak_hmac("good", 'no', ipad, opad)
