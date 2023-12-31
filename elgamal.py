import random

from squareandmultiply import sqandmult
from multiplicativeinverse import multinv
from generator import generate
from primefactorization import prime
from alphanumeric import numeric
from alphanumeric import alpha



def setup(p,g):
    '''Setting up Public Key'''
   
    print("Choose random number b")
    b = random.randint(2,p-2)

    B = sqandmult(g,b,p)

    return B, b

def encrypt(g,p,B,m):
    '''Encryption'''
    C =[]

    print("Choose random number a")
    a = random.randint(2,p-2)

    Keph = sqandmult(g,a,p)

    K = sqandmult(B,a,p)

    for i in m:
        C.append((i*K)%p)
    
    
    # C = (m*K)%p

    return Keph, C


def decrypt(Keph,b,C,p):

    m2 =[]

    K = sqandmult(Keph,b,p)

    print("This is K: ", K)


    kinv = multinv(p,K)

    for i in C:
        m2.append((i*kinv)%p)
    # m2 = (C*kinv)%p

    return m2



if __name__ == '__main__':

    print("Choose large prime p")
    p = int(input())

    pf = prime(p)

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
    # m = int(input())

    M = input()
    OM = M
    
    M = numeric(M)
    print(M)

    Keph, C = encrypt(g,p,B,M)

    m2 = decrypt(Keph,b,C,p)
    m2 =alpha(m2)
    # print(M2)

    if OM == m2:
        print("It worked: ", OM)
    else:
        print("Didn't work", OM, m2)
