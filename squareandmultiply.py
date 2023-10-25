
def mval(m,b):
    '''Find the value of m'''
    m = (m-b)//2
    return m

def bit(m):
    ''' Find the binary value'''    
    b= m % 2
    return b 


def sqandmult(u,m,p):
    '''Square and Multiply Algorithm'''
    A = 1
    sqround = 1
    print("Round: ", sqround)
    b = bit(m)
    usquare = 1
    asquare = 0

    if b == 0:
        '''print("m = ", m ,", b = ", b, ", u = ", u , ", A = ", A, " A square = ", asquare, " Skip")'''
        print()
    else:
        A = (A*u) % p
        asquare = usquare+asquare
        '''print("m = ", m ,", b = ", b, ", u = ", u , "Squaring: ...",  ", A = ", A ," A square =", asquare, " Multiply" )'''

    m = mval(m,b)
    sqround+=1
    
    
    
    while m != 1:
        print("Round: ", sqround)
        b = bit(m)

        if b == 0:
            usquare*=2
    
            u = (u**2) % p
            '''print("m = ", m ,", b = ", b, ", u = ", u , "Squaring: ", usquare ,", A = ", A ," A square =", asquare, " Multiply" )'''
        else:
            usquare*=2
            u = (u**2) % p
            A = (A*u) % p
            asquare = usquare+asquare
            '''print("m = ", m ,", b = ", b, ", u = ", u , "Squaring: ", usquare ,", A = ", A ," A square =", asquare, " Multiply" )'''
        
        m = mval(m,b)
        sqround+=1
    
    '''b = bit(m)'''
    u = (u**2) % p
    A = (A*u) % p
    asquare = usquare+asquare
    '''print("m = ", m ,", b = ", b, ", u = ", u , "Squaring: ", usquare ,", A = ", A ," A square =", asquare, " Multiply" )'''

    return A
