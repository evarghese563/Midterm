'''Finding the gcd of 2 numbers to check if it's coprime'''

import math

print("Enter val1")
val1 = int(input())

print("Enter val2")
val2 = int(input())

gcd = math.gcd(val1,val2)

if gcd == 1:
    print("Coprime: ", gcd)
else:
    print("Not Coprime: ", gcd)