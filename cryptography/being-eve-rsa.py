''' being-eve-rsa.py
    By: Zack Johnson
    Brute forces the p and q values used to choose an n in the RSA Encryption.
'''

def main():
    # Find primes p and q
    n = 5561
    p, q = bruteForcePrimeFactors(n)
    print("For n =", n)
    print("P:", p, "and Q:", q)

    # Find the decryption number d
    e = 13
    lambdaN = 2706
    d = bruteForceSecretKey(e, lambdaN)
    print("For e =", e, "and lam =", lambdaN)
    print("d:", d)

    # Decrypt a message
    message = getMessage()
    plain_text = decryptRSA(d, n, message)
    print(plain_text)

    # convert to ascii
    string = ''.join(chr(i) for i in plain_text)
    print(string)

def bruteForcePrimeFactors(n):
    primes = getPrimesUnder(n)
    for prime in primes:
        if( n % prime == 0):
            return prime, n/prime

def getPrimesUnder(n):
    numbers = range(2, n, 1)
    primes = []
    for number in numbers:
        is_prime = True
        for prime in primes:
            if (number % prime == 0):
                is_prime = False
        if is_prime:
            primes.append(number)
    return primes

def bruteForceSecretKey(e, lambdaN):
    for d in range(lambdaN):
        if (e*d % lambdaN == 1):
            return d

def decryptRSA(d, n, message):
    plain_text = []
    for char in message:
        plain_text.append(char ** d % n)
    return plain_text

def getMessage():
    return [1516, 3860, 2891, 570, 3483, 4022, 3437, 299,
 570, 843, 3433, 5450, 653, 570, 3860, 482,
 3860, 4851, 570, 2187, 4022, 3075, 653, 3860,
 570, 3433, 1511, 2442, 4851, 570, 2187, 3860,
 570, 3433, 1511, 4022, 3411, 5139, 1511, 3433,
 4180, 570, 4169, 4022, 3411, 3075, 570, 3000,
 2442, 2458, 4759, 570, 2863, 2458, 3455, 1106,
 3860, 299, 570, 1511, 3433, 3433, 3000, 653,
 3269, 4951, 4951, 2187, 2187, 2187, 299, 653,
 1106, 1511, 4851, 3860, 3455, 3860, 3075, 299,
 1106, 4022, 3194, 4951, 3437, 2458, 4022, 5139,
 4951, 2442, 3075, 1106, 1511, 3455, 482, 3860,
 653, 4951, 2875, 3668, 2875, 2875, 4951, 3668,
 4063, 4951, 2442, 3455, 3075, 3433, 2442, 5139,
 653, 5077, 2442, 3075, 3860, 5077, 3411, 653,
 3860, 1165, 5077, 2713, 4022, 3075, 5077, 653,
 3433, 2442, 2458, 3409, 3455, 4851, 5139, 5077,
 2713, 2442, 3075, 5077, 3194, 4022, 3075, 3860,
 5077, 3433, 1511, 2442, 4851, 5077, 3000, 3075,
 3860, 482, 3455, 4022, 3411, 653, 2458, 2891,
 5077, 3075, 3860, 3000, 4022, 3075, 3433, 3860,
 1165, 299, 1511, 3433, 3194, 2458]

if __name__ == "__main__":
    main()
