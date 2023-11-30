import re

#open files
starting_point = "#import molang/myscript.molang"
file = open("./regolith/molang/myscript.molang","r").read()

def getFilePath(tokens):
    path = ""
    end_index = 0
    #paths can start with ./molang/, /molang/, molang/, 
    #paths must end with .molang

    return (path,end_index)

def getMolangString(file):
    content = open(file).read()
    define_name = re.findall("molang/[a-zA-Z1-9_\-/]+\.molang",file)[0]
    define_name = "_" + re.sub("[/\.]","_",define_name).upper()
    return "#ifndef " + define_name + "\n#define " + define_name + "\n" + content + "\n#endif"

#tokenizer
def getTokens(string):
    return re.findall("(file|[A-Za-z_]+[A-Za-z0-9_]*|\*/|/\*|,|\.|\?|:|;|//|\+=|-=|\*=|/=|\+\+|\+|\*|-|/|<|>|<=|>=|==|!=|&&|\|\||=|\d+\.?\d+|#|\(|\{|\[|'|\"|\)|\}|\]|\n|.)",string)

#removes any comments
def filterComments(tokens):
    is_comment = False
    is_multiline_comment = False
    is_string = False
    x = 0
    while x < len(tokens):
        token = tokens[x]
        if token == "//":
            if not is_comment and not is_multiline_comment and not is_string:
                is_comment = True
        if token == "\n":
            if is_comment:
                is_comment = False
                tokens.pop(x)
                x -= 1
        if token == "/*":
            if not is_multiline_comment and not is_comment and not is_string:
                is_multiline_comment = True
        if token == "*/":
            if is_multiline_comment:
                tokens.pop(x)
                x -= 1
                is_multiline_comment = False
        if token == "\"" or token == "\'":
            if not is_multiline_comment and not is_comment and not is_string:
                is_string = True
            if is_string:
                is_string = False
        if is_comment or is_multiline_comment:
            tokens.pop(x)
            x -= 1
        x += 1
            
#combines any tokens found within a string (remove comments before doing this)
def combineStrings(tokens):
    is_string = False
    x = 0
    while x < len(tokens):
        token = tokens[x]
        if token == "\"" or token == "\'":
            is_string = not is_string
        elif is_string and tokens[x+1] != "\"" and tokens[x+1] != "\'":
            tokens[x + 1] += tokens[x] 
            tokens.pop(x)
            x -= 1
        x += 1

#returns all preprocessor commands
def groupTokens(tokens):
    groups = {}
    for x in range(len(tokens)):
        if tokens[x] == "#":
            
    #label things with identifier, literal, etc
    #group preprocessor
    #group functions
    #group function headers
    #group operations


#builds tokens into a labeled tree
#def sort_tokens(tokens):


#preprocessor

#tokens = getTokens(starting_point)

#insert implicit preprocessor defines
#default_defines = open("./regolith/molang/default_defines.molang","r").read()
#tokens.insert(0,getTokens(default_defines))

#1. build tokens from imports
#2. apply if and define statements
#3. parse

#file = open("./regolith/" + getFilePath(tokens[i:i+20]))
#filestring = file.read()
#filetokens = getTokens(filestring)

tokens = getTokens(getMolangString("./regolith/molang/myscript.molang"))
filterComments(tokens)
combineStrings(tokens)
print(tokens)