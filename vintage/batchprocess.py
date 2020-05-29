import os
import colors
# import generate


def batchColors():
    for subdir, dirs, files in os.walk("./dataset"):
        for filename in files:
            # print os.path.join(subdir, file)
            filepath = subdir + os.sep + filename
            if (filepath.endswith(".jpeg") or filepath.endswith(".png") or
                    filepath.endswith(".jpg")):
                print(filepath)
                colors.start(filepath, 10)


def batchGenerate():
    for subdir, dirs, files in os.walk("./dataset"):
        for filename in files:
            # print os.path.join(subdir, file)
            filepath = subdir + os.sep + filename
            if (filepath.endswith(".txt")):
                print(filepath)
                # generate.Generate(filepath)


batchColors()
