import math
from squareandmultiply import sqandmult
from multiplicativeinverse import multinv

def encrypt(M,e,n):
    '''In Encrypt'''

    # C = (M**e) % n
    C = sqandmult(M,e,n)
    print("This is C", C)
    return C

def decrypt(C,d,n):
    '''In Decrpyt'''

    # M = (C**d) % n
    M = sqandmult(C,d,n)
    # print("this is M", M)

    return M





if __name__ == '__main__':
    
    print("Input Prime Number P")
    p = int(input())

    print("Input Prime Number q")
    q = int(input())

    print("Enter Message")

    M = int(input())
    
    n = p*q

    phin = (p-1)*(q-1)
    print("phi n is: ", phin)
    coprime = 0
    
    while coprime != 1:
    
        print("Enter e")
        e = int(input())

        coprime = math.gcd(e,phin)
        # print(coprime)

    
    
    print("Enter multiplicative inverse of e")

    d = multinv(phin,e)
    # d = int(input())

    C = encrypt(M,e,n)

    M2 = decrypt(C,d,n)

    print(M2)

    if M == M2:
        print("Original Message: ", M)
    else:
        print("Broken try again", M, M2)