import os
import re
print(os.getcwd())

file = open("./regolith/molang/myscript.molang","r").read()
file2 = open("./regolith/molang/default_defines.molang","r").read()

defines_pos = re.findall("\n#define (.+) as (.*)",file2)
for pos in defines_pos:
    print(pos)
    #re.sub(pos[0], pos[1], file)
#defines stop at //, /*, \n

print("read function: ")
print(file)