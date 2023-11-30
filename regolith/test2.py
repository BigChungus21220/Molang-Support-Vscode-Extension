import re

starting_point = "#import molang/myscript.molang"
file = open("./regolith/molang/myscript.molang","r").read()

def getMolangString(file):
    content = open(file).read()
    define_name = re.findall("molang/[a-zA-Z1-9_\-/]+\.molang",file)[0]
    define_name = "_" + re.sub("[/\.]","_",define_name).upper()
    return "#ifndef " + define_name + "\n#define " + define_name + "\n" + content + "\n#endif"

grammar = {
    "word": "[A-Za-z_][A-Za-z0-9_]*",
    "string": "([\"].*[\"])|([\'].*[\'])",
    "comment": "(/\*.*\*/)|(//.*\n)",
    "number": "[1-9]\d*(\.\d+)?",
    "bool": "true|false",
    "macro": "#word.*\n",
    "function": "word\(.*\)",
    "variable": "word",
    "expression": "function|string|number|variable|bool",
    "divide": "expession/expression",
    "multiply": "expession*expression",
    "subtract": "expession-expression",
    "add": "expession+expression",
    "mod": "expression%expression",
    "declaration": "func|var|vec|arr|tmp word = expression"
}