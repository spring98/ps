import random
import sys
sys.setrecursionlimit(2000)  # default = 1000: sys.getrecursionlimit()

"""
GCD(assume a>=0, b>=0 )
"""
def gcd(a, b):
    if a < b:
        a, b = b, a
    if a == b:
        return a
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)


"""
Extended Euclidean Algorithm (Iterative version) ( a >= b )

return (x, y, r) such that a * x + b * y = r = gcd(a, b)
loop invariant :
a * x_1 + b * y_1 = r_1
a * x_2 + b * y_2 = r_2

"""
def extended_euclid(a, b):

    if a == b:
        return 1, 0, a
    elif b == 0:
        return 1, 0, a
    else:
        x_1 = 1
        y_1 = 0
        r_1 = a

        x_2 = 0
        y_2 = 1
        r_2 = b

        while r_2 != 0:
            q = r_1 // r_2

            r_t = r_1 - q * r_2
            x_t = x_1 - q * x_2
            y_t = y_1 - q * y_2

            x_1, y_1, r_1 = x_2, y_2, r_2
            x_2, y_2, r_2 = x_t, y_t, r_t

        return x_1, y_1, r_1


"""
Multiplicative Inverse

x = a^-1 mod n 
a * x mod n = 1

"""
def m_inv(a, n):
    x, y, r = extended_euclid(n, a % n)
    if r != 1:
        print("No multiplicative inverse")
        return
    else:
        return y % n

"""
miller-rabin prime test
Test if n is prime with error probability less than 1/2^n.
"""
Prime = 0
Composite = 1
def miller_rabin(n, s):
    if n == 2:
        return Prime
    elif n % 2 == 0:
        return Composite

    for _ in range(s):
        a = random.randint(1, n-1)
        if test(a, n) == True:
            return Composite

    return Prime

"""
subroutine for miller-rabin prime test
Perform the Fermat test and NSR (nontrivial square root) test.
"""
def test(a, n):
    bits = int_to_bin(n-1)
    k = len(bits) - 1
    t = 0

    while bits[k] == '0':
        t += 1
        k -= 1

    u = (n-1) >> t     # n - 1 is represented as u * (2**t)
    x = exp(a, u, n)
    for _ in range(t):
        _x = x
        x = (_x * _x) % n
        if x == 1 and _x != 1 and _x != n-1:
            return True

    if x != 1:
        return True
    else:
        return False

"""
int_to_bin
convert an integer to a binary representation
(the most significant bit becomes the 0-th bit)
"""
def int_to_bin(num):
    return list(bin(num))[2:]

"""
Modular exponentiation
returns a ^ b mod n
Left ro Right version
def exp(a, b, n):
    c = 0
    f = 1
    bin_b = int_to_bin(b)
    k = len(bin_b)
    for i in range(k):
        c = 2 * c
        f = (f * f) % n
        if bin_b[i] == '1':
            c = c + 1
            f = (f * a) % n
    return f
"""

"""
Modular exponentiation
returns a ^ b mod n
Right to Left version
"""
def exp(a, b, n):
    t = a
    f = 1
    bin_b = int_to_bin(b)
    k = len(bin_b)
    for i in range(k):
        if bin_b[k-i-1] == '1':
            f = (f * t) % n
        t = (t * t) % n
    return f

"""
RSA key pair generation
keylen: security parameter (desired number of bits in n)
    (keylen > 4)
"""
def keygen(keylen):
    bound = 1 << keylen//2   # upper bound for p and q.
    p = 2 * random.randint(bound//4, bound//2) - 1       # guarantee that p is odd.
    while miller_rabin(p, 50) == Composite:
        p = 2 * random.randint(bound//4, bound//2) - 1   # select new odd p.
    q = 2 * random.randint(bound//4, bound//2) - 1       # guarantee that q is odd.
    while miller_rabin(q, 50) == Composite:
        q = 2 * random.randint(bound//4, bound//2) - 1   # select new odd q.
    # Now p and q are odd primes.
    n = p * q
    phi_n = (p-1) * (q-1)
    e = 2*random.randint(1, phi_n//2) - 1        # guarantee that e is odd.
    while gcd(phi_n, e) != 1:
        e = 2*random.randint(1, phi_n//2) - 1    # select new odd e.
    d = m_inv(e, phi_n)
    #print("p, q, n, phi(n), e, d: %d, %d, %d, %d, %d, %d" % (p, q, n, phi_n, e, d))
    return (e, d, n)


"""
RSA encryption
e, n: public key
M: plaintext < n
"""
def encrypt(M, e, n):
    return exp(M, e, n)

"""
RSA decryption
d, n: private key
C: ciphertext < n
"""
def decrypt(C, d, n):
    return exp(C, d, n)

"""
RSA test
"""
if __name__ == "__main__":
    e, d, n = keygen(128)
    M = 89
    C = encrypt(M, e, n)
    MM = decrypt(C, d, n)
    if M == MM:
        print("Example of RSA Algorithm works successfully")
        print("M={}, PU=({},{}), PR=({},{}), C={}, MM={}".format(M, e, n, d, n, C, MM))
    else:
        print("Example of RSA Algorithm fails")
        print("M={}, PU=({},{}), PR=({},{}), C={}, MM={}".format(M, e, n, d, n, C, MM))
