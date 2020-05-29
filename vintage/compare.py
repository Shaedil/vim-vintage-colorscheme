###########################################################
# compare.py -Script that compares any two painting's hex
#             hex values for similarity or rank in the
#             frequency list and quantifies it with a
#             percentage
# Author:  Shaedil Dider
# Last Change: 2020 May 27
###########################################################
import colors as col


def compare(file1, file2):
    # Extract the two color sets and put them in a variable
    # Process them into RGB>LAB values using colors library
    # Comparison algorithm using delta E algorithm
    # https://stackoverflow.com/a/52453462/6273236
    hex1colorlist = eval(open("./dataset/" + file1).read())
    hex2colorlist = eval(open("./dataset/" + file2).read())
    lab1colorList = []
    lab2colorList = []
    for i in range(0, len(hex1colorlist)):
        x = hex1colorlist[i]
        x = col.hexToRGB(x)
        x = col.rgb2lab(x)
        lab1colorList.append(x)
        y = hex2colorlist[i]
        y = col.hexToRGB(y)
        # y = col.rgb2lab(y)
        lab2colorList.append(y)
    print(lab1colorList)
    print(lab2colorList)


compare('monalisa.txt', 'belle.txt')
