###########################################################
# compare.py -Script that compares any two painting's hex
#             hex values for similarity or rank in the
#             frequency list and quantifies it with a
#             percentage
# Author:  Shaedil Dider
###########################################################

import colors
from statistics import mean

# Extract the two color sets and put them in a variable
# Process them into RGB>LAB values using colors library
# Comparison algorithm using delta E algorithm
# https://stackoverflow.com/a/52453462/6273236


def compareTwoColorSets(firstFile, secondFile):

    firstColorSet = eval(open("./dataset/" + firstFile).read())
    secondColorSet = eval(open("./dataset/" + secondFile).read())
    convertedFirstColorSet = convertColorSetToLAB(firstColorSet)
    convertedSecondColorSet = convertColorSetToLAB(secondColorSet)

    meanSimilarityBetweenBothColorSets = calculateMeanSimularityOfTwoColorSets(convertedFirstColorSet, convertedSecondColorSet)

    return printLevelOfPerceptibility(meanSimilarityBetweenBothColorSets)


def convertColorSetToLAB(inputColorSet):
    colorSetInLAB = []
    for eachColorScheme in inputColorSet:
        eachColorSchemeInRBG = colors.hexToRGB(eachColorScheme)
        eachColorSchemeInLAB = colors.rgb2lab(eachColorSchemeInRBG)
        colorSetInLAB.append(eachColorSchemeInLAB)
    return colorSetInLAB.sort()


def calculateMeanSimularityOfTwoColorSets(firstColorSetInLAB, secondColorSetInLAB):
    arrayOfSimilarities = []
    totalNumberOfColors = len(firstColorSetInLAB)
    for eachColor in range(totalNumberOfColors):
        firstColorToCompare = firstColorSetInLAB[eachColor]
        secondColorToCompare = secondColorSetInLAB[eachColor]
        similarityBetweenTwoColors = colors.deltaE(firstColorToCompare, secondColorToCompare)
        arrayOfSimilarities.append(similarityBetweenTwoColors)
    return mean(arrayOfSimilarities)


def printLevelOfPerceptibility(meanSimilarityBetweenBothColorSets):
    if (meanSimilarityBetweenBothColorSets <= 1.0):
        print("Delta E:    <= 1.0")
        print("Perception: The difference in the color set of the paintings are not perceptible by human eyes")
        return
    if (meanSimilarityBetweenBothColorSets <= 2.0):
        print("Delta E:    1 - 2")
        print("Perception: The difference in the color set of the paintings are perceptible through close observation")
        return
    if (meanSimilarityBetweenBothColorSets <= 11.0):
        print("Delta E:    2 - 10")
        print("Perception: The difference in the color set of the paintings are perceptible at a glance")
        return
    if (meanSimilarityBetweenBothColorSets <= 49.0):
        print("Delta E:    11 - 49")
        print("Preception: The color set of the paintings are more similar than opposite")
        return
    else:
        print("Delta E:    49 - 100")
        print("Perception: The color set of the paintings are exact opposites")
        return
