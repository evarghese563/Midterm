import random

from squareandmultiply import sqandmult
from multiplicativeinverse import multinv
from generator import generate
from primefactorization import prime

def setup(p,g):
    '''Setting up Public Key'''
   
    print("Choose random number b")
    b = random.randint(2,p-2)

    # b = 61
    # B = (g**b)%p
    B = sqandmult(g,b,p)

    return B, b

def encrypt(g,p,B,m):
    '''Encryption'''
   
    print("Choose random number a")
    a = random.randint(2,p-2)

    # a= 4

    # Keph = (g**a)%p

    Keph = sqandmult(g,a,p)

    # K = (B**a)%p

    K = sqandmult(B,a,p)

    C = (m*K)%p

    return Keph, C

def decrypt(Keph,b,C,p):

    # K = (Keph**b) % p
    K = sqandmult(Keph,b,p)
    print("This is K: ", K)
    # print("Input Multplicative Inverse of K")
    # kinsv = int(input())

    kinv = multinv(p,K)

    m2 = (C*kinv)%p

    return m2



if __name__ == '__main__':

    print("Choose large prime p")
    p = int(input())

    pf = prime(p)

    print("Choose generator g")
    # g = int(input())


    print("input generator")
    temp = int(input())
    flag = 1

    while flag ==1:
        flag = generate(temp, p, pf)
        
        if flag == 1:
            print("input generator")
            temp = int(input())
    
    g = temp
    print()
    print("GENERATOR: ", g)
    print()

    B,b = setup(p,g)

    print("Public Key: ", p , g, B)

    print()
    print("Input Message")
    m = int(input())

    Keph, C = encrypt(g,p,B,m)

    m2 = decrypt(Keph,b,C,p)

    if m == m2:
        print("It worked: ", m)
    else:
        print("Didn't work")
