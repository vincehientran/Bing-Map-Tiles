from TileSystem import TileSystem as ts
import urllib.request as ul
import cv2
import numpy as np
import sys

def run(lat1, long1, lat2, long2):
    URLstart = 'http://ecn.t0.tiles.virtualearth.net/tiles/h'
    URLend = '.jpeg?g=129&mkt=en-US&shading=hill&stl=H'

    # get the bounding lat/long pixels, tiles, and quadkeys
    pixelX1, pixelY1 = ts.latlongToPixelXY(lat1, long1, 20)
    tileX1, tileY1 = ts.pixelXYToTileXY(pixelX1, pixelY1)
    quadKey1 = ts.tileXYToQuadKey(tileX1, tileY1, 20)

    pixelX2, pixelY2 = ts.latlongToPixelXY(lat2, long2, 20)
    tileX2, tileY2 = ts.pixelXYToTileXY(pixelX2, pixelY2)
    quadKey2 = ts.tileXYToQuadKey(tileX2, tileY2, 20)

    colCount = tileX2 - tileX1 + 1
    rowCount = tileY2 - tileY1 + 1

    # store quadkeys of all tiles in the bounding box
    quadKeys = [['' for _ in range(colCount)] for _ in range(rowCount)]
    for i in range(len(quadKeys)):
        for j in range(len(quadKeys[0])):
            tileY = tileY1 + i
            tileX = tileX1 + j
            quadKeys[i][j] = ts.tileXYToQuadKey(tileX, tileY, 20)

    # request an image of each tile in the bounding box
    imageArray = [[None for _ in range(colCount)] for _ in range(rowCount)]
    for i in range(len(quadKeys)):
        for j in range(len(quadKeys[0])):
            quadKey = quadKeys[i][j]
            URL = URLstart + quadKey + URLend
            resp = ul.urlopen(URL)
            tempImage = np.asarray(bytearray(resp.read()), dtype="uint8")
            tempImage = cv2.imdecode(tempImage, cv2.IMREAD_COLOR)
            imageArray[i][j] = tempImage

    # concatenate all images into one image
    rowImages = []
    for i in range(len(imageArray)):
        rowImage = None
        for j in range(len(imageArray[0])):
            if j == 0:
                rowImage = imageArray[i][j]
            else:
                rowImage = np.concatenate((rowImage, imageArray[i][j]), axis = 1)

        rowImages.append(rowImage)

    image = None
    for i in range(len(rowImages)):
        if i == 0:
            image = rowImages[i]
        else:
            image = np.concatenate((image, rowImages[i]), axis = 0)

    # crop the image to the exact pixel of the bounding lat/long coords
    topLeftX, topLeftY = pixelX1 % 256, pixelY1 % 256
    botRightX, botRightY = 256 - (pixelX2 % 256), 256 - (pixelY2 % 256)
    height = len(image) - topLeftY - botRightY
    width = len(image[0]) - topLeftX - botRightX
    image = image[topLeftY : topLeftY + height, topLeftX : topLeftX + width]

    cv2.imwrite('output.jpg', image)

if __name__ == '__main__':
    if (len(sys.argv) == 5) :
        lat1, long1, lat2, long2 = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
        run(lat1, long1, lat2, long2)
    else:
        print('Enter the lat1, lon1, lat2, lon2 as the program arguments. ')
