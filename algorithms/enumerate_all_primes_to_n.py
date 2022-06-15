# Write a program that takes an integer argument and returns all the primes between 1 and that integer.
# For example, if the input is 18, you should return [2, 3, 5, 7, 11, 13, 17].
# A natural number is called a prime if it is bigger than 1 and has no divisors other than 1 and itself.


# Brute-force solution
def generate_primes_brute_force(n):
    primes = []
    for i in range(2, n + 1):
        for p in range(2, i + 1):
            if p == i:
                primes.append(i)
                break
            if i % p == 0:
                break
    return primes


# A better approach is to compute the primes and when a number is identified as a prime,
# to "sieve" it, i.e., remove all its multiples from future consideration.
def generate_primes(n):
    primes = []
    # is_prime[p] represents if p is prime or not. Initially, set each to
    # true, expecting 0 and 1. IIen use sieving to eliminate non-primes.
    is_prime = [False, False] + [True] * (n - 1)
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p, n + 1, p):
                is_prime[i] = False
    return primes


print(generate_primes(18))
print(generate_primes_brute_force(18))
