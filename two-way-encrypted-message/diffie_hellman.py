import random
'''
Global Parameters
1. q = Large Prime Number
2. a = Primitive root of q
Logic behind Diffie-Hellman Key Exchange
1. Private Key = Random Number i.e. x
2. Public Key = (a^x) mod q
Shared Key = ((Public Key of B) ^ Private Key of A) mod q
'''


def getLargePrimeNumber(lowerLimit, upperLimit):
    '''
    A utility function to help generate a global parameter,
    the large prime number
    '''
    p = 2
    upperLimit = max(upperLimit, 2)
    isPrime = [False] * 2 + [True] * (upperLimit - 1)
    while (p ** 2 < upperLimit):
        if isPrime[p]:
            for i in range(p ** 2, upperLimit + 1, p):
                isPrime[i] = False

        p += 1

    result = [i for i, check in enumerate(isPrime) if check and i > lowerLimit]
    return random.choice(result)


def getPrimitiveRoot(q, reverse=False):
    '''
    Primitive root of a prime number is another number which
    generate all remainders possible with respect to this prime
    number when powers of the root is raised to all the values
    less than the prime number
    Eg. For q=7, the remainders would be: [1,2,3...6]
    The primitive root for 11 is 3
    2 mod 7 = 2
    4 mod 7 = 3
    8 mod 7 = 1
    16 mod 7 = 2 --> Repeated so it is not.
    3 mod 7 = 3
    9 mod 7 = 2
    27 mod 7 = 6
    81 mod 7 = 4
    243 mod 7 = 5
    729 mod 7 = 1
    All the remainders produced, so 3 is a primitive root of 7
    '''
    if isPrime(q):
        test = set()
        pos = [x for x in range(2, q)]
        if reverse:
            pos = pos[::-1]

        for num in pos:
            for i in range(1, q):
                val = (num ** i) % q
                if val in test:
                    test = set()
                    break
                else:
                    test.add(val)

                if len(test) == q - 1:
                    return num
    else:
        print("Entered number is not prime: No primitive root")
        return None


def keyGeneration(number, root, privateKeyLimit=101):
    '''
    Given the global parameters i.e. the large prime
    number (number) and the primitive root (root),
    the public and private key are generated. An optional
    argument, privateKeyLimit, is used to set the upper
    limit, any number within the range of 100 less than
    would be taken as the private key
    '''
    privateKeyLimit = max(privateKeyLimit, 101)
    private = random.randint(privateKeyLimit - 100, privateKeyLimit)
    public = (root ** private) % number
    return (private, public)


def sharedKeyGeneration(publicKey, privateKey, number):
    return (publicKey ** privateKey) % number


def isPrime(number):
    '''
    The Key Exchange is based on the selection of the large
    prime number as the security lies in the discrete logarithm
    '''
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


if __name__ == '__main__':
    print("This is just a collection of functions needed for Diffie-Hellman Key Exchange Implementation")
