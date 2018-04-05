#!/usr/bin/env python3

from string import ascii_letters, digits, punctuation

message = 'rases are...'
ALPHABET = digits + ascii_letters

def ceasar(crypted, offset, backwards=False):
	x = (-1) ** backwards # 1 if False, -1 if True

	decrypted = ""

	for pos in range(len(crypted)):
		char = crypted[pos]
		if char in punctuation or char == ' ':
			decrypted += char
			continue
		index = ALPHABET.find(char)
		decrypted += ALPHABET[(index + x*offset) % len(ALPHABET)]

	return decrypted


def vigenere(crypted, key, backwards=False):

	decrypted = ""

	for pos in range(len(crypted)):
		offset = ALPHABET.find(key[pos % len(key)])
		decrypted += ceasar(crypted[pos], offset, backwards)

	return decrypted




