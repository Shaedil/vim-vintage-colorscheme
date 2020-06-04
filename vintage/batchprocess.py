########################################################
# batchProcess.py - Script that performs processes in
#                   batches on multiple files at once.
# Author:  Shaedil Dider
# Last Change: 2020 May 17
########################################################
import os
from sklearn.cluster import KMeans
import numpy as np
import colors as col
# import generate
# import compare


def batchColors():
    for subdir, dirs, files in os.walk("./dataset"):
        for filename in files:
            filepath = subdir + os.sep + filename
            if (filepath.endswith(".jpeg") or filepath.endswith(".png") or
                    filepath.endswith(".jpg")):
                print(filepath)
                filename = filepath.rsplit('/', 1)[1]
                fp = filepath.rsplit('/', 1)[0]
                col.start(fp + '/' + filename, 10)


def batchGenerate():
    for subdir, dirs, files in os.walk("./dataset"):
        for filename in files:
            filepath = subdir + os.sep + filename
            if (filepath.endswith(".txt")):
                print(filepath)
                # generate.Generate(filepath)


def catPalettes():
    for subdir, dirs, files in os.walk("./dataset"):
        try:
            x = './dataset/' + subdir.rsplit('/', 2)[2]
            print(x)
            os.system('cat ' + x + '/*.txt >' + x + '.txt')
            os.system('cat ' + x + '/*.txt >' + x + '.txt')
        except IndexError:
            pass


def appendLists():
    for subdir, dirs, files in os.walk("./dataset"):
        try:
            x = './dataset/' + subdir.rsplit('/', 2)[2] + '.txt'
            with open(x, "r") as f:
                lines = [eval(line.rstrip()) for line in f]
            print(lines, file=open(x, "w"))
        except IndexError:
            pass


def batchCompare(X):
    kmeans = KMeans(n_clusters=10).fit(X)  # X = data
    colors = kmeans.cluster_centers_
    return colors.astype(int)


def start():
    for subdir, dirs, files in os.walk("./dataset"):
        try:
            x = './dataset/' + subdir.rsplit('/', 2)[2] + '.txt'
            w = './dataset/' + subdir.rsplit('/', 2)[2] + '-Analysis.txt'
            print("output: " + w)
            x = eval(open(x).read())
            y = []
            for listofhexval in x:
                for hexval in listofhexval:
                    z = col.rgb2lab(col.hexToRGB(hexval))
                    y.append([round(i, 3) for i in z])
            y = col.toMatrix(y, 10)
            # TODO: order y by frequency by calling the histogram function
            # in colors.py or creating it here
            # FIXME: y is not of the correct shape. Have it so that it's
            # like this: [[ (10 col) ], [ (10 col) ], [ (10 col) ]]
            y = np.asarray(y, dtype=np.float32)
            print(y.shape)
            y = y.transpose(2, 0, 1).reshape(10, -1)
            print(y)
            # y = batchCompare(y).tolist()
            # print(y, file=open(w, "w"))
        except IndexError:
            pass


start()
