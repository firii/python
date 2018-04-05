#!/usr/bin/env python3
#Usage: randtabl.py <cols> <rows> [min] [max]

from sys import argv
import random
from math import log10

def get_int(argIndex, msg, default=None):

    result = None

    try:
        result = int(argv[argIndex])
    
    except IndexError:
        while result is None:
            try:
                inp = input(msg)
                result = int(inp)

            except ValueError:
                if inp != '':
                    print('Incorrect input, use only numbers.')
                else:
                    result = default
    
    except ValueError as ve2:
        if default is None:
            print('Usage: randtabl.py <cols> <rows> [min] [max]\n', ve2)
            exit()
        
        result = default

    return result

rand = random.Random()

cols = get_int(1, 'cols: ')
rows = get_int(2, 'rows: ')
minValue = get_int(3, 'min or [Enter] for 0: ', 0)
maxValue = get_int(4, 'max or [Enter] for 1000:', 1000)

width = int(log10(max(maxValue, abs(minValue)))) + 2

for x in range(0, rows):
    for y in range(0, cols):
        cellValue = rand.randint(minValue, maxValue)
        print(("{0:>{1}}").format(cellValue, width), end=' ')
    print()

