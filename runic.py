#!/usr/bin/env python3
#Usage: runic.py <input> [output] [dictionary]

from sys import argv

runes =   '᛫ᚠᚡᚢᚣᚤᚥᚦᚧᚨᚩᚪᚫᚬᚭᚮᚯᚰᚱᚲᚳᚴᚵᚶᚷᚸᚹᚺᚻᚼᚽᚾᚿᛀᛁᛂᛃᛄᛅᛆᛇᛈᛉᛊᛋᛌᛍᛎᛏᛐᛑᛒᛓᛔᛕᛖᛗᛘᛙᛚᛛᛜᛝᛞᛟᛠᛡᛢᛣ'
letters = ' !"#$%&\'()*+,-./0123456789:;<=>?@[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

def hasAny(data, chars):
    """Returns True if data contains any character from chars"""
    for l in chars:
        if l in data:
            return True
    return False

if len(argv) > 1:
    try:
        with open(argv[1], 'r') as data:
            input_data = data.read().lower()
            out_name = data.name
            data.close()
    except Exception as e:
        print('File not found')
        exit()
else:
    print('Usage: runic.py <input> [output] [dictionary]')
    exit()

if len(argv) > 2:
    out_name = argv[2]

if len(argv) > 3:
    try:
        with open(argv[3], 'r') as data:
            runes, letters = data.readlines()
            data.close()
    except Exception as e:
        print('Dictionary not found')
        exit()

if hasAny(input_data, letters) and not hasAny(input_data, runes):
    table = "".maketrans(letters, runes)
    out_name = 'runic_' + out_name

elif hasAny(input_data, runes) and not hasAny(input_data, letters):
    table = "".maketrans(runes, letters)
    out_name = 'eng_' + out_name

else:
    print('No symbols to encrypt/decrypt')
    exit()

out_data = input_data.translate(table)
out_file = open(out_name, 'w')
out_file.write(out_data)
out_file.close()



