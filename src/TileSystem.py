import math

class TileSystem():
    EARTH_RADIUS = 6378137
    MIN_LAT = -85.05112878
    MAX_LAT = 85.05112878
    MIN_LONG = -180
    MAX_LONG = 180

    def clip(n, minValue, maxValue):
        return math.min(math.max(n, minValue), maxValue)

    def tileXYToQuadKey(tileX, tileY, levelOfDetail):
        quadKey = ''

        for i in range(levelOfDetail, 0, -1):
            digit = 0
            mask = 1 << (i - 1)

            if ((tileX & mask) != 0):
                digit += 1

            if ((tileY & mask) != 0):
                digit += 2

            quadKey += str(digit)

        return quadKey
