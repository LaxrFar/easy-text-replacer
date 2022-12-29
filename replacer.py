import sys
import fileinput
import json

replacefile = input("In what file you want it to replace: ")

config = open('config.json')

data = json.load(config)

orginal = data['orginal']
replace = data['replace']
f = open(replacefile, "r+")


for l in fileinput.input(files = replacefile):
    l = l.replace(orginal, replace)
    f.write(l)

f.close