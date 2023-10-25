import math
from squareandmultiply import sqandmult
from multiplicativeinverse import multinv
from alphanumeric import numeric
from alphanumeric import alpha

def encrypt(M,e,n):
    '''In Encrypt'''
    C = []
    # C = (M**e) % n
    
    for i in M:
        C.append(sqandmult(i,e,n))
    
    # C = sqandmult(M,e,n)
    # print("This is C", C)
    return C

def decrypt(C,d,n):
    '''In Decrpyt'''
    M2 = []
    # M = (C**d) % n
    for i in C:
        M2.append(sqandmult(i,d,n))
    # M = sqandmult(C,d,n)
    # print("this is M", M)

    return M2





if __name__ == '__main__':
    
    print("Input Prime Number P")
    p = int(input())

    print("Input Prime Number q")
    q = int(input())

    n = p*q

    phin = (p-1)*(q-1)
    print("phi n is: ", phin)

    print("Enter Message")
    M = input()
    OM = M
    
    M = numeric(M)
    print(M)

    
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
    print(C)

    M2 = decrypt(C,d,n)

    M2 =alpha(M2)
    print(M2)

    if OM == M2:
        print("Original Message: ", M)
    else:
        print("Broken try again", M, M2)