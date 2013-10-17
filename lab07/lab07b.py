# Program to generate a list of primes using the Sieve of Eratosthenes
# Sample run:
# Input a positive integer n: 20
# [1, 2, 3, 5, 7, 11, 13, 17, 19]

def init(n):
    '''Return a list of size n; each element "unmarked".'''
    init_list=[]
    for i in range(n):
        init_list.append(i)
    return init_list

def sieve(L):
    '''Modify L to be a list with primes "unmarked" (use Sieve of Eratosthenes).'''
    for i in range(2, len(L)):
            for n in range(2, len(L)):     # Mark factors non-prime
                if i*n >= len(L):
                    break
                L[i*n]=1
    return L

def make_prime_list(L):
    '''Using L, return a list of primes.'''
    primes_list=[]
    for i in range(len(L)):
        if L[i]==0:
            primes_list.append(i)
    return primes_list
    

n = int(input("Input a positive integer n: "))
L = init(n)
sieve(L)
primes_list = make_prime_list(L)
print(primes_list)
