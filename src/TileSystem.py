import math

class TileSystem():
    EARTH_RADIUS = 6378137
    MIN_LAT = -85.05112878
    MAX_LAT = 85.05112878
    MIN_LONG = -180
    MAX_LONG = 180

    def clip(n, minValue, maxValue):
        return min(max(n, minValue), maxValue)

    def mapSize(levelOfDetail):
        return 256 << levelOfDetail

    def latlongToPixelXY(lat, long, levelOfDetail):
        lat = TileSystem.clip(lat, TileSystem.MIN_LAT, TileSystem.MAX_LAT)
        long = TileSystem.clip(long, TileSystem.MIN_LONG, TileSystem.MAX_LONG)

        x = (long + 180) / 360
        sinLat = math.sin(lat * math.pi / 180)
        y = 0.5 - math.log((1 + sinLat) / (1 - sinLat)) / (4 * math.pi)

        size = TileSystem.mapSize(levelOfDetail)
        pixelX = int(TileSystem.clip(x * size + 0.5, 0, size - 1))
        pixelY = int(TileSystem.clip(y * size + 0.5, 0, size - 1))

        return pixelX, pixelY

    def pixelXYToTileXY(pixelX, pixely):
        tileX = int(pixelX / 256)
        tileY = int(pixely / 256)
        return tileX, tileY

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
