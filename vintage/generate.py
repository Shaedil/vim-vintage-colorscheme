########################################################
# Generate.py - Script that generates vim colorschemes
#               with pre-generated hex color codes.
# Author:  Shaedil Dider
# Last Change: 2020 Sept 23
########################################################
import fileinput
import shutil
import os
import colors as col


def Generate(filename):
    # Grabs filename* colors and assign each to a key in colorDict
    filen = filename.rsplit('.', 1)
    colorList = eval(open("./" + filename).read())
    filename = filen[0] + ".vim"
    keys = ('\"a\"', '\"b\"', '\"c\"', '\"d\"', '\"e\"', '\"f\"',
            '\"g\"', '\"h\"', '\"i\"', '\"j\"', '\"k\"')
    # values = ('\"'+col.bestMatch(colors)+'\",' for colors in colorList)
    values = ('\"'+colors+'\"' for colors in colorList)
    colorDict = dict(zip(keys, values))
    print(colorDict)  # For debugging purposes
    shutil.copy2("./tempactual.vim", "./" + filename)
    for letter in list(map(chr, range(97, 108))):
        letter = '\"' + letter + '\"'
        traverseAndReplace(filename, letter, colorDict.get(letter))
    removeEmptyLines(filename)


def traverseAndReplace(fileIn, findString, replaceString):
    # search and replace text inside file
    for line in fileinput.input(files=(fileIn), inplace=True):
        line = line.replace(findString, replaceString)
        print(line)


def removeEmptyLines(filename):
    if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    with open(filename) as filehandle:
        lines = filehandle.readlines()
    with open(filename, 'w') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines)


# For debugging purposes
Generate('color.txt')
