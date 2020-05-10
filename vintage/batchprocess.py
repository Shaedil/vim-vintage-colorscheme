import os
import colors

for subdir, dirs, files in os.walk("."):
    for filename in files:
        # print os.path.join(subdir, file)
        filepath = subdir + os.sep + filename
        if (filepath.endswith(".jpeg") or filepath.endswith(".png") or
                filepath.endswith(".jpg")):
            print(filepath)


# for loop here ... iterate through number of images in a folder
# call start() function with every image filename.jpeg
