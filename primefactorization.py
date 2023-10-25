from math import sqrt


def primefactor(n):
    i = 2
    factors = []
    
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def isprime(n):
 
    if (n <= 1):
        return False
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            return False
 
    return True
 

# if __name__ == '__main__':

#     print("Input Number")
#     n = int(input())

def prime(n):

    if isprime(n):
        n = n-1
        factors = primefactor(n)
        return factors
    else:
        print("number is not prime")