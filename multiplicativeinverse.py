
def tfunc(t1,t2, q ):
    '''Calculate T'''
    t = t1 - t2*q
    return t

def multinv(a,b):
    '''Function where you find the multiplicative inverse'''

    p = a
    temp = b 
    q = 0
    r = 0
    t1 = 0
    t2 = 1
    t = 0
    while(b != 0 ):

        if b != 0 :
            q = a//b
            r = a % b
            t = tfunc(t1,t2,q)

            a = b
            b = r
            t1 = t2
            t2 = t
        else:
            a = b
            b = r
            t1 = t2
            t2 = t
    if t1 > 0:
        print("Mod Inverse")
        print(t1)   
        return t1
    else:
        # print("Mod Inverse")
        return t1+p
