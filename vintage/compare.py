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


def compare_color_sets(first_file, second_file):
    color_set1 = eval(open("./dataset/" + first_file).read())
    color_set2 = eval(open("./dataset/" + second_file).read())
    converted_set1 = convert_color_set_to_LAB(color_set1)
    converted_set2 = convert_color_set_to_LAB(color_set2)

    mean_similarity = calculate_mean_simularity(converted_set1, converted_set2)
    print_level_of_perceptibility(mean_similarity)

def convert_color_set_to_LAB(input_color_set):
    color_set_in_LAB = []
    for each_color_scheme in input_color_set:
        each_color_scheme_in_RBG = colors.hexToRGB(each_color_scheme)
        each_color_scheme_in_LAB = colors.rgb2lab(each_color_scheme_in_RBG)
        color_set_in_LAB.append(each_color_scheme_in_LAB)
    return color_set_in_LAB.sort()


def calculate_mean_simularity(color_set_in_LAB1, color_set_in_LAB2):
    similarities = []
    for color1, color2 in zip(color_set_in_LAB1, color_set_in_LAB2):
        similarity_between_colors = colors.deltaE(color1, color2)
        similarities.append(similarity_between_colors)
    return mean(similarities)

def print_level_of_perceptibility(mean_similarity):
    if mean_similarity <= 1.0:
        print("Delta E:    <= 1.0")
        print(
            "Perception: The difference in the color set of the paintings are not perceptible by human eyes"
        )
    elif mean_similarity <= 2.0:
        print("Delta E:    1 - 2")
        print(
            "Perception: The difference in the color set of the paintings are perceptible through close observation"
        )
    elif mean_similarity <= 11.0:
        print("Delta E:    2 - 10")
        print(
            "Perception: The difference in the color set of the paintings are perceptible at a glance"
        )
    elif mean_similarity <= 49.0:
        print("Delta E:    11 - 49")
        print(
            "Preception: The color set of the paintings are more similar than opposite"
        )
    else:
        print("Delta E:    49 - 100")
        print("Perception: The color set of the paintings are exact opposites")
