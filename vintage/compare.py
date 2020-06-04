###########################################################
# compare.py -Script that compares any two painting's hex
#             hex values for similarity or rank in the
#             frequency list and quantifies it with a
#             percentage
# Author:  Shaedil Dider
# Last Change: 2020 May 27
###########################################################
import colors as col
from statistics import mean


def compare(file1, file2):
    # Extract the two color sets and put them in a variable
    # Process them into RGB>LAB values using colors library
    # Comparison algorithm using delta E algorithm
    # https://stackoverflow.com/a/52453462/6273236
    hex1colorlist = eval(open("./dataset/" + file1).read())
    hex2colorlist = eval(open("./dataset/" + file2).read())
    lab1colorList = []
    lab2colorList = []
    # processing
    for i in range(0, len(hex1colorlist)):
        x = hex1colorlist[i]
        x = col.hexToRGB(x)
        x = col.rgb2lab(x)
        lab1colorList.append(x)
        y = hex2colorlist[i]
        y = col.hexToRGB(y)
        y = col.rgb2lab(y)
        lab2colorList.append(y)
    # sort colors to be compared evenly
    similitudefactor = []
    lab1colorList.sort()
    lab2colorList.sort()
    for i in range(0, len(lab1colorList)):
        x = lab1colorList[i]
        y = lab2colorList[i]
        z = col.deltaE(x, y)
        similitudefactor.append(z)
    print(mean(similitudefactor))
    if (mean(similitudefactor)) <= 1.0:
        print("Delta E:    <= 1.0")
        print("Perception: The difference in the color set of the paintings are not perceptible by human eyes")
    elif (1 < (mean(similitudefactor)) and mean(similitudefactor) <= 2):
        print("Delta E:    1 - 2")
        print("Perception: The difference in the color set of the paintings are perceptible through close observation")
    elif (2 < (mean(similitudefactor)) and mean(similitudefactor) <= 11):
        print("Delta E:    2 - 10")
        print("Perception: The difference in the color set of the paintings are perceptible at a glance")
    elif (11 < (mean(similitudefactor)) and mean(similitudefactor) <= 49):
        print("Delta E:    11 - 49")
        print("Preception: The color set of the paintings are more similar than opposite")
    else:
        print("Delta E:    49 - 100")
        print("Perception: The color set of the paintings are exact opposites")


compare('monalisa.txt', 'belle.txt')
