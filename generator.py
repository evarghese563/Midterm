'''Finding the the generator for DH/El Gamal'''


from squareandmultiply import sqandmult



def generate(g, p, pf):

    flag = 0  
   
    for q in pf:

        exponent = (p-1)/q
        
        val = sqandmult(g,exponent,p)


        if val == 1:
            flag = 1

    return flag

