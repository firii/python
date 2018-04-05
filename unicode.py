#!/usr/bin/env python3

runes = ''
asci = ''
for index in range(0x16a0, 0x16f1):
	runes += chr(index)
for index in range(0x20, 0x7f):
	asci += chr(index)
out = open('unicoded.txt', mode='w', encoding='utf-8')
out.write(runes + '\n' + asci)
out.close()