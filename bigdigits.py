#!/usr/bin/env python3
from sys import argv

digits = {}
digits['0'] = [' ## ', '#  #', '#  #', '#  #', '#  #', '#  #', ' ## ']
digits['1'] = ['   #', '  ##', ' # #', '   #', '   #', '   #', '   #']
digits['2'] = [' ## ', '   #', '   #', ' ## ', '#   ', '#   ', ' ## ']
digits['3'] = [' ## ', '#  #', '   #', '  # ', '   #', '#  #', ' ## ']
digits['4'] = ['#  #', '#  #', '#  #', ' ###', '   #', '   #', '   #']
digits['5'] = [' ## ', '#   ', '#   ', ' ## ', '   #', '   #', ' ## ']
digits['6'] = [' ## ', '#   ', '#   ', ' ## ', '#  #', '#  #', ' ## ']
digits['7'] = ['####', '   #', '   #', '  # ', ' #  ', ' #  ', ' #  ']
digits['8'] = [' ## ', '#  #', '#  #', ' ## ', '#  #', '#  #', ' ## ']
digits['9'] = [' ## ', '#  #', '#  #', ' ## ', '   #', '   #', ' ## ']

try:
	if len(argv) >= 3:
		symbol = argv[2][0]
	else:
		symbol = '#'

	for i in range(0, 7):
		line = ''
		for digit in argv[1]:
			line += digits[digit][i] + '  '
		print(line.replace('#', symbol))

except IndexError as ie:
	print('Usage: bigdigits.py <number> [symbol]')

except KeyError as ke:
	print('"{}" is not a digit'.format(digit))