'''Finding the the generator for DH/El Gamal'''

import numpy as np
from squareandmultiply import sqandmult


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

def generate(p, pf):

    flag = 0  
    print("input prime number between 1 and p-1")
    g = int(input())

    for q in pf:

        exponent = (p-1)/q

        # val = (g**exponent) % p

        val = sqandmult(g,exponent,p)

        # print(val)

        if val == 1:
            flag = 1
        
    
    if flag == 1:
        generate(p,pf)
    else:
        print("This is your generator: ", g)

    


if __name__ == '__main__':

    print("Input your prime number")
    p = int(input())

    pf = primefactor(p-1)

    generate(p, pf)

    # print("This is your generator: ", g)