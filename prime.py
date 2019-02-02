import random

# test if a large number is prime with Miller-Rabin algorithm
def miller_rabin(n, k = 40):
    if n == 2 or n == 3 :
        return True
    if n % 2 == 0 or n < 2:
        return False
    r = 0
    s = n - 1
    while s % 2 == 0:
        r += 1
        s = s // 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# generate a bits sized random number
def generate_random_number(bits):
    return random.getrandbits(bits)

# generate a bits sized random prime
def generate_random_prime(bits):
    x = generate_random_number(bits)
    while not miller_rabin(x):
        x = x+1
    return x

# # generate two bits sized random primes
def generate_two_random_prime(bits):
    x = generate_random_prime(bits)
    y = generate_random_prime(bits)
    if x == y:
        generate_two_random_prime(bits)
    else:
        return (x, y)






    
