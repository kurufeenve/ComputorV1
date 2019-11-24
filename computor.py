#!/usr/bin/python3

import sys
import re

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
print (type(sys.argv))

equation = sys.argv[1]

print (equation)
print (type(equation))

parts = list()
signs = list()
filler = ' '
previous_sign = 0
i = 0
j = 0
for letter in equation:
    if letter == '+':
        parts.append(equation[previous_sign:i])
        signs.append('+')
        previous_sign = i + 1
    elif letter == '-':
        parts.append(equation[previous_sign:i])
        signs.append('-')
        previous_sign = i + 1
    elif letter == '=':
        parts.append(equation[previous_sign:i])
        equation2 = equation[i+1:]
        signs.append('-')
        previous_sign = 0
        for letter2 in equation2:
            if (letter2 == '='):
                print ("\nequation is incorrect. second '=' at", i + j,'\n')
                print (equation)
                print (filler * (i + j),'^')
                sys.exit()
            elif letter2 == '+':
                parts.append(equation2[previous_sign:j])
                signs.append('-')
                previous_sign = j + 1
            elif letter2 == '-':
                parts.append(equation2[previous_sign:j])
                signs.append('+')
                previous_sign = j + 1
            j = j + 1
        parts.append(equation2[previous_sign:])
        break
    i = i + 1
print(parts,'\n',signs)

