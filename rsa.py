import random
import decimal_string
import prime

# greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# check if a and b coprimes
def coprime(a, b):
    return gcd(a, b) == 1

# the extended euclidean algorithm to find the private key
def extended_euclidean_alg(a, b):
    x, y = a, b
    t0, t1 = 0, 1
    r, t = b, 1
    while (x % y) != 0:
        q = x // y
        r = x % y
        t = (t0 - q*t1) % a
        x = y
        y = r
        t0 = t1
        t1 = t
    return t

# generation of private and public key from two primes
def generate_keys():
    p, q = prime.generate_two_random_prime(512)
    n = p * q
    phi = (p-1)*(q-1)
    e = random.randrange(1, phi)
    while not coprime(e, phi):
        e = random.randrange(1, phi)
    d = extended_euclidean_alg(phi, e)
    return ((e, n), (d, n))

# encrypyt max 128 length ascii text
def encrypt(public_key, text):
    e, n = public_key
    text_number = decimal_string.text_to_integer(text)
    encoded = pow(text_number, e, n)
    return encoded

# decrypt ascii text
def decrypt(private_key, text_number):
    d, n = private_key
    decoded = pow(text_number, d, n)
    return decimal_string.integer_to_text(decoded)
