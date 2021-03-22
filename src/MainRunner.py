from TileSystem import TileSystem as ts

def run(lat1, long1, lat2, long2):
    pixelX1, pixelY1 = ts.latlongToPixelXY(lat1, long1, 20)
    tileX1, tileY1 = ts.pixelXYToTileXY(pixelX1, pixelY1)
    quadKey1 = ts.tileXYToQuadKey(tileX1, tileY1, 20)

    pixelX2, pixelY2 = ts.latlongToPixelXY(lat2, long2, 20)
    tileX2, tileY2 = ts.pixelXYToTileXY(pixelX2, pixelY2)
    quadKey2 = ts.tileXYToQuadKey(tileX2, tileY2, 20)

    print(quadKey1)
    print(tileX1, tileY1)

    print(quadKey2)
    print(tileX2, tileY2)

    rowCount = tileX2 - tileX1
    colCount = tileY2 - tileY1

    quadKeys = [['' for _ in range(colCount)] for _ in range(rowCount)]
    for i in range(len(quadKeys)):
        for j in range(len(quadKeys[0])):
            tileX = tileX1 + i
            tileY = tileY1 + j
            quadKey = ts.tileXYToQuadKey(tileX1, tileY1, 20)

if __name__ == '__main__':
    run(41.98303725364395, -87.69917964935303, 41.97587910570054, -87.68914282321931)
