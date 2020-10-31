########################################################
# batchProcess.py - Script that performs processes in
#                   batches on multiple files at once.
# Author:  Shaedil Dider
########################################################

import os
from sklearn.cluster import KMeans
import numpy as np
import colors as col
from colors import DominantColors
import generate
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
                generate.Generate(filepath)


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


def batchCompare(X, n):
    kmeans = KMeans(n_clusters=n).fit(X)  # X = data
    colors = kmeans.cluster_centers_
    # implement delta E in distance calculation
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
            y = np.asarray(y)
            n = int(y.size/30)
            y = y.transpose(2, 0, 1).reshape(n, -1)
            y = batchCompare(y, n).tolist()
            a = [y[i][j:j + 3] for i in range(len(y)) for j in range(0,
                                                                     len(y[i]),
                                                                     3)]
            # b = [a[n:n+10] for n in range(0, len(a), 10)]
            # print(b)
            # print(batchCompare(a, 10).tolist(), file=open(w, "w"))
            c = batchCompare(a, 10).tolist()
            dc = DominantColors(c, 10)
            dc.plotClusters()
            # print(a, file=open(w, "w"))
        except IndexError:
            pass


start()
