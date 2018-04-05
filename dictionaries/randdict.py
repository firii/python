#!/usr/bin/env python3
#Usage: randdict.py

from random import Random

rand = Random()

name = 'dict' + hex(rand.randint(0x1000, 0xffff))
runes = 'ᚠᚡᚢᚣᚤᚥᚦᚧᚨᚩᚪᚫᚬᚭᚮᚯᚰᚱᚲᚳᚴᚵᚶᚷᚸᚹᚺᚻᚼᚽᚾᚿᛀᛁᛂᛃᛄᛅᛆᛇᛈᛉᛊᛋᛌᛍᛎᛏᛐᛑᛒᛓᛔᛕᛖᛗᛘᛙᛚᛛᛜᛝᛞᛟᛠᛡᛢᛣ'
letters = ' !"#$%&\'()*+,-./0123456789:;<=>?@[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

runeList = [c for c in runes]
rand.shuffle(runeList)
runes = '᛫' + ''.join(runeList)

f = open(name, 'w')
f.write(runes + '\n' + letters)
f.close()
