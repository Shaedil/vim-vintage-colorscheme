import matplotlib.pyplot as plt
import cv2
import numpy as np
from sty import bg, rs
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans


class DominantColors:

    CLUSTERS = None
    IMAGE = None
    COLORS = None
    LABELS = None

    def __init__(self, image, clusters):
        self.CLUSTERS = clusters
        self.IMAGE = image

    def rgbToHex(self, rgb):
        # converts from RGB to Hex, not for graphing the histogram
        hexColors = []
        for i in range(len(rgb)):
            r = rgb[i][0]
            g = rgb[i][1]
            b = rgb[i][2]
            hexColor = '#%02x%02x%02x' % (r, g, b)
            hexColors.append(hexColor)
        return hexColors

    # for graphing color
    def rgb_to_hex(self, rgb):
        return '#%02x%02x%02x' % (int(rgb[0]), int(rgb[1]), int(rgb[2]))

    def hexToRGB(self, value):
        # works for one hex value at a time
        h = value.strip('#')
        x = int(h[0:2], 16)
        y = int(h[2:4], 16)
        z = int(h[4:6], 16)
        return [x, y, z]

    def printColor(self, rgb):
        for CLUSTERS in range(len(rgb)):
            r = int(rgb[CLUSTERS][0])
            g = int(rgb[CLUSTERS][1])
            b = int(rgb[CLUSTERS][2])
            foo = bg(r, g, b) + '                        ' + rs.bg
            print(str(CLUSTERS+1) + foo)

    def plotClusters(self):
        fig = plt.figure()
        ax = Axes3D(fig)
        for label, pix in zip(self.LABELS, self.IMAGE):
            ax.scatter(pix[0], pix[1], pix[2],
                       color=self.rgb_to_hex(self.COLORS[label]))
        plt.show()

    def plotHistogram(self):
        # labels form 0 to no. of clusters
        numLabels = np.arange(0, self.CLUSTERS+1)
        # create frequency count tables
        (hist, _) = np.histogram(self.LABELS, bins=numLabels)
        hist = hist.astype("float")
        hist /= hist.sum()
        # appending frequencies to cluster centers
        colors = self.COLORS
        # descending order sorting as per frequency count
        colors = colors[(-hist).argsort()]
        hist = hist[(-hist).argsort()]
        return(colors)

    def dominantColors(self):
        img = cv2.imread(self.IMAGE)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img.reshape((img.shape[0] * img.shape[1], 3))
        self.IMAGE = img
        kmeans = KMeans(n_clusters=self.CLUSTERS)
        kmeans.fit(img)
        self.COLORS = kmeans.cluster_centers_
        self.LABELS = kmeans.labels_
        return self.COLORS.astype(int)


def start():
    # obtain the img.jpeg from the relative path
    img = str(input("What is the input image's relative path?: "))
    filename = img.rsplit('/', 1)  # remove .jpeg from img
    filen = filename[1].rsplit('.', 1)
    try:
        f = open(filen[0] + ".txt")  # parse file
        stringColorList = f.read()  # a string representation of a list
        hexcolorlist = eval(stringColorList)  # convert to actual list
        # print the colors from the file
        dc = DominantColors(img, len(hexcolorlist))
        # From here one out, requires rgb
        rgbcolorList = []
        for i in range(0, len(hexcolorlist[0])):
            x = hexcolorlist[0][i]
            x = dc.hexToRGB(x)
            rgbcolorList.append(x)
        print(dc.printColor(rgbcolorList))
        print(hexcolorlist[0])
        f.close()
    except FileNotFoundError:
        # The intermediary file does not exist
        print("File not accessible or found... creating new file instead")
        clusters = int(input("What is the desired number of colors?: "))
        dc = DominantColors(img, clusters)
        colors = dc.dominantColors()  # color = list of rgb colors
        
        intermediaryColors = colors.tolist()  # nd array to plain list
        intermediaryColors = dc.rgbToHex(intermediaryColors)
        finalColors = []  # an empty list in which values will go into
        with open(filen[0] + ".txt", "a") as f:
            finalColors.append(intermediaryColors)
            print(finalColors, file=f)
            # write list of rgb colors to a new file
        print(dc.printColor(colors))
        print(dc.rgbToHex(colors))


img = '../Documents/LaTeX/Pre-Calculus/colors.jpeg'
clusters = 5
dc = DominantColors(img, clusters)
colors = dc.dominantColors()
print(dc.plotHistogram())
# start()
