alphabetUpper = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23 ,
    'X': 24,
    'Y': 25,
    'Z': 26,
}
alphabetLower = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22 ,
    'x': 23,
    'y': 24,
    'z': 25,
}

numericUpper={
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E',
    6: 'F',
    7: 'G',
    8: 'H',
    9: 'I',
    10: 'J',
    11: 'K',
    12: 'L',
    13: 'M',
    14: 'N',
    15: 'O',
    16: 'P',
    17: 'Q',
    18: 'R',
    19: 'S',
    20: 'T',
    21: 'U',
    22: 'V',
    23: 'W' ,
    24: 'X',
    25: 'Y',
    26: 'Z',
}

def numeric(m):
    '''Function to find Numeric Expression of the message'''
    num = []

    for i in m:
        try:
            num.append(alphabetUpper[i])
        except Exception as e:
            num.append(alphabetLower[i])
    
    return num


def alpha(num):
    alphabet = []

    for i in num:
        try:
            alphabet.append(numericUpper[i])
        except Exception as e:
            alphabet.append(numericUpper[i])
    return alphabet

# if __name__ == '__main__':
#     print("Input Message M")
#     m = input()
#     m = list(m)
#     # print(m)


#     num = numeric(m)
#     print("Numeric Expression of the message")
#     print(num)

#     print()
#     alpha(num)

