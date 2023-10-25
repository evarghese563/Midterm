import random

from squareandmultiply import sqandmult
from multiplicativeinverse import multinv
from generator import generate
from primefactorization import prime
from alphanumeric import numeric
from alphanumeric import alpha
import math




def signing(r,k,p,g):

    R = random.randint(0,p-1)

    coprime = 0
    
    while coprime != 1:

        R = random.randint(0,p-1)
        coprime = math.gcd(R,p-1)
    
    x = sqandmult(g,k,p)
    
    
    #M =rX +RY

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

    r = random.randint(0,p-1)

    k = sqandmult(g,r,p)

    print("Input Message")

    M = int(input())
    
    Msig = signing(r,k,p,g)







    B,b = setup(p,g)

    print("Public Key: ", p , g, B)

    print()
    print("Input Message")
    # m = int(input())

    M = int(input())
    # OM = M
    
    # M = numeric(M)
    # print(M)

    Keph, C = encrypt(g,p,B,M)

    m2 = decrypt(Keph,b,C,p)
    m2 =alpha(m2)
    # print(M2)

    if OM == m2:
        print("It worked: ", OM)
    else:
        print("Didn't work", OM, m2)