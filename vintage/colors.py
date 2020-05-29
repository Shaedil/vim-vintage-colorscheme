########################################################
# Colors.py - Script that obtains set of frequent colors
#             in order of frequency using KMeans library
# Author:  Shaedil Dider
# Last Change: 2020 May 17
########################################################
import matplotlib.pyplot as plt
import cv2
import numpy as np
import math
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
        # converts from RGB to Hex, not for graphing the
        # histogram
        hexColors = []
        for i in range(len(rgb)):
            r = rgb[i][0]
            g = rgb[i][1]
            b = rgb[i][2]
            hexColor = '#%02x%02x%02x' % (r, g, b)
            hexColors.append(hexColor)
        return hexColors

    def rgb_to_hex(self, rgb):
        # for graphing color
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
        numLabels = self.CLUSTERS
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


def toMatrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]


def start(img, clusters):
    # img is defined as the relative path
    filename = img.rsplit('/', 1)  # remove .jpeg from img
    filen = filename[1].rsplit('.', 1)
    try:
        f = open("./dataset/" + filen[0] + ".txt")  # parse file
        stringColorList = f.read()  # a string representation of a list
        hexcolorlist = eval(stringColorList)  # convert to actual list
        # init class with list
        dc = DominantColors(img, len(hexcolorlist))
        # From here on out, requires rgb
        rgbcolorList = []
        for i in range(0, len(hexcolorlist)):
            x = hexcolorlist[i]
            x = dc.hexToRGB(x)
            rgbcolorList.append(x)
        print(dc.printColor(rgbcolorList))
        print(hexcolorlist)
        f.close()
    except FileNotFoundError:
        # The intermediary file does not exist
        print("File not accessible or found... creating new file instead")
        dc = DominantColors(img, clusters)
        colors = dc.dominantColors()  # colors = list of rgb colors
        colors = dc.plotHistogram()  # sort the generated list of colors
        intermediaryColors = colors.tolist()  # nd array to plain list
        intermediaryColors = toMatrix([round(y) for x in
                                       range(len(intermediaryColors))
                                       for y in intermediaryColors[x]], 3)
        intermediaryColors = dc.rgbToHex(intermediaryColors)
        with open("./dataset/" + filen[0] + ".txt", "w") as f:
            # write list of rgb colors to a new file
            print(intermediaryColors, file=f)
        print(dc.printColor(colors))
        print(intermediaryColors)


def hexToRGB(value):
    # works for one hex value at a time
    h = value.strip('#')
    x = int(h[0:2], 16)
    y = int(h[2:4], 16)
    z = int(h[4:6], 16)
    return [x, y, z]

colors = {
    '000000':  '16', '00005f':  '17', '000087':  '18', '0000af':  '19',
    '0000d7':  '20', '0000ff':  '21', '005f00':  '22', '005f5f':  '23',
    '005f87':  '24', '005faf':  '25', '005fd7':  '26', '005fff':  '27',
    '008700':  '28', '00875f':  '29', '008787':  '30', '0087af':  '31',
    '0087d7':  '32', '0087ff':  '33', '00af00':  '34', '00af5f':  '35',
    '00af87':  '36', '00afaf':  '37', '00afd7':  '38', '00afff':  '39',
    '00d700':  '40', '00d75f':  '41', '00d787':  '42', '00d7af':  '43',
    '00d7d7':  '44', '00d7ff':  '45', '00ff00':  '46', '00ff5f':  '47',
    '00ff87':  '48', '00ffaf':  '49', '00ffd7':  '50', '00ffff':  '51',
    '5f0000':  '52', '5f005f':  '53', '5f0087':  '54', '5f00af':  '55',
    '5f00d7':  '56', '5f00ff':  '57', '5f5f00':  '58', '5f5f5f':  '59',
    '5f5f87':  '60', '5f5faf':  '61', '5f5fd7':  '62', '5f5fff':  '63',
    '5f8700':  '64', '5f875f':  '65', '5f8787':  '66', '5f87af':  '67',
    '5f87d7':  '68', '5f87ff':  '69', '5faf00':  '70', '5faf5f':  '71',
    '5faf87':  '72', '5fafaf':  '73', '5fafd7':  '74', '5fafff':  '75',
    '5fd700':  '76', '5fd75f':  '77', '5fd787':  '78', '5fd7af':  '79',
    '5fd7d7':  '80', '5fd7ff':  '81', '5fff00':  '82', '5fff5f':  '83',
    '5fff87':  '84', '5fffaf':  '85', '5fffd7':  '86', '5fffff':  '87',
    '870000':  '88', '87005f':  '89', '870087':  '90', '8700af':  '91',
    '8700d7':  '92', '8700ff':  '93', '875f00':  '94', '875f5f':  '95',
    '875f87':  '96', '875faf':  '97', '875fd7':  '98', '875fff':  '99',
    '878700': '100', '87875f': '101', '878787': '102', '8787af': '103',
    '8787d7': '104', '8787ff': '105', '87af00': '106', '87af5f': '107',
    '87af87': '108', '87afaf': '109', '87afd7': '110', '87afff': '111',
    '87d700': '112', '87d75f': '113', '87d787': '114', '87d7af': '115',
    '87d7d7': '116', '87d7ff': '117', '87ff00': '118', '87ff5f': '119',
    '87ff87': '120', '87ffaf': '121', '87ffd7': '122', '87ffff': '123',
    'af0000': '124', 'af005f': '125', 'af0087': '126', 'af00af': '127',
    'af00d7': '128', 'af00ff': '129', 'af5f00': '130', 'af5f5f': '131',
    'af5f87': '132', 'af5faf': '133', 'af5fd7': '134', 'af5fff': '135',
    'af8700': '136', 'af875f': '137', 'af8787': '138', 'af87af': '139',
    'af87d7': '140', 'af87ff': '141', 'afaf00': '142', 'afaf5f': '143',
    'afaf87': '144', 'afafaf': '145', 'afafd7': '146', 'afafff': '147',
    'afd700': '148', 'afd75f': '149', 'afd787': '150', 'afd7af': '151',
    'afd7d7': '152', 'afd7ff': '153', 'afff00': '154', 'afff5f': '155',
    'afff87': '156', 'afffaf': '157', 'afffd7': '158', 'afffff': '159',
    'd70000': '160', 'd7005f': '161', 'd70087': '162', 'd700af': '163',
    'd700d7': '164', 'd700ff': '165', 'd75f00': '166', 'd75f5f': '167',
    'd75f87': '168', 'd75faf': '169', 'd75fd7': '170', 'd75fff': '171',
    'd78700': '172', 'd7875f': '173', 'd78787': '174', 'd787af': '175',
    'd787d7': '176', 'd787ff': '177', 'd7af00': '178', 'd7af5f': '179',
    'd7af87': '180', 'd7afaf': '181', 'd7afd7': '182', 'd7afff': '183',
    'd7d700': '184', 'd7d75f': '185', 'd7d787': '186', 'd7d7af': '187',
    'd7d7d7': '188', 'd7d7ff': '189', 'd7ff00': '190', 'd7ff5f': '191',
    'd7ff87': '192', 'd7ffaf': '193', 'd7ffd7': '194', 'd7ffff': '195',
    'ff0000': '196', 'ff005f': '197', 'ff0087': '198', 'ff00af': '199',
    'ff00d7': '200', 'ff00ff': '201', 'ff5f00': '202', 'ff5f5f': '203',
    'ff5f87': '204', 'ff5faf': '205', 'ff5fd7': '206', 'ff5fff': '207',
    'ff8700': '208', 'ff875f': '209', 'ff8787': '210', 'ff87af': '211',
    'ff87d7': '212', 'ff87ff': '213', 'ffaf00': '214', 'ffaf5f': '215',
    'ffaf87': '216', 'ffafaf': '217', 'ffafd7': '218', 'ffafff': '219',
    'ffd700': '220', 'ffd75f': '221', 'ffd787': '222', 'ffd7af': '223',
    'ffd7d7': '224', 'ffd7ff': '225', 'ffff00': '226', 'ffff5f': '227',
    'ffff87': '228', 'ffffaf': '229', 'ffffd7': '230', 'ffffff': '231',
    '080808': '232', '121212': '233', '1c1c1c': '234', '262626': '235',
    '303030': '236', '3a3a3a': '237', '444444': '238', '4e4e4e': '239',
    '585858': '240', '626262': '241', '6c6c6c': '242', '767676': '243',
    '808080': '244', '8a8a8a': '245', '949494': '246', '9e9e9e': '247',
    'a8a8a8': '248', 'b2b2b2': '249', 'bcbcbc': '250', 'c6c6c6': '251',
    'd0d0d0': '252', 'dadada': '253', 'e4e4e4': '254', 'eeeeee': '255',
}


def Decompose(hexval):
    hexval = hexval.strip('#')
    return float(int(hexval[0:2], 16)), float(int(hexval[2:4], 16)), float(int(hexval[4:6], 16))


def Normalize(r, g, b):
    magsqr = r*r + g*g + b*b
    if magsqr < 0.0001:
        return 0.0, 0.0, 0.0
    n = 1.0 / math.sqrt(magsqr)
    return r*n, g*n, b*n


def colorDist(c1, c2):
    c1r, c1g, c1b = Decompose(c1)
    c2r, c2g, c2b = Decompose(c2)
    dr = c1r - c2r
    dg = c1g - c2g
    db = c1b - c2b
    return dr*dr + dg*dg + db*db


def bestMatch(hexval):
    best = None
    bestdist = 0.0
    for key in colors.keys():
        dist = colorDist(hexval, key)
        if best is None or dist < bestdist:
            best = colors[key]
            bestdist = dist
    return best


def rgb2lab(rgb):
    r = rgb[0] / 255
    g = rgb[1] / 255
    b = rgb[2] / 255
    x = 0
    y = 0
    z = 0
    r = (r > 0.04045) if (math.pow((r + 0.055) / 1.055, 2.4)) else r / 12.92
    g = (g > 0.04045) if (math.pow((g + 0.055) / 1.055, 2.4)) else g / 12.92
    b = (b > 0.04045) if (math.pow((b + 0.055) / 1.055, 2.4)) else b / 12.92
    x = (r * 0.4124 + g * 0.3576 + b * 0.1805) / 0.95047
    y = (r * 0.2126 + g * 0.7152 + b * 0.0722) / 1.00000
    z = (r * 0.0193 + g * 0.1192 + b * 0.9505) / 1.08883
    x = (x > 0.008856) if math.pow(x, 1/3) else (7.787 * x) + 16/116
    y = (y > 0.008856) if math.pow(y, 1/3) else (7.787 * y) + 16/116
    z = (z > 0.008856) if math.pow(z, 1/3) else (7.787 * z) + 16/116
    return [(116 * y) - 16, 500 * (x - y), 200 * (y - z)]


def deltaE(labA, labB):
    deltaL = labA[0] - labB[0]
    deltaA = labA[1] - labB[1]
    deltaB = labA[2] - labB[2]
    c1 = math.sqrt(labA[1] * labA[1] + labA[2] * labA[2])
    c2 = math.sqrt(labB[1] * labB[1] + labB[2] * labB[2])
    deltaC = c1 - c2
    deltaH = deltaA * deltaA + deltaB * deltaB - deltaC * deltaC
    deltaH = deltaH < 0 if 0 else math.sqrt(deltaH)
    sc = 1.0 + 0.045 * c1
    sh = 1.0 + 0.015 * c1
    deltaLKlsl = deltaL / (1.0)
    deltaCkcsc = deltaC / (sc)
    deltaHkhsh = deltaH / (sh)
    i = deltaLKlsl * deltaLKlsl + deltaCkcsc * deltaCkcsc + deltaHkhsh * deltaHkhsh
    return i < 0 if 0 else math.sqrt(i)
