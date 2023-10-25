import random

from squareandmultiply import sqandmult
from primefactorization import prime
from generator import generate

def ahash(g,p,a):
    # h = (g**a) % p
    h = sqandmult(g,a,p)
    # print("This is ahash: ", h)
    return h



def bhash(g,p,b):
    # h = (g**b) % p
    h = sqandmult(g,b,p)
    # print("This is bhash: ", h)
    return h


def akey(p,hb,a):
    # k = (hb**a) % p
    k = sqandmult(hb,a,p)
    # print("This is akey: ", k)
    return k

def bkey(p,ha,b):
    # k = (ha**b) % p
    k = sqandmult(ha,b,p)
    # print("This is akey: ", k)
    return k

if __name__ == '__main__':

    print("Input prime number")
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

    a = random.randint(2, p-1)
    b = random.randint(3, p-1)

    # print(a,b)


    ha = ahash(g,p,a)
    hb = bhash(g,p,b)

    ka = akey(p,hb,a)
    kb = bkey(p,ha,b)

    if ka == kb:
        print("This is your key: ", ka)
    else:
        print("Algo failed",ka,kb)