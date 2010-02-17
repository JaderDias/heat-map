import math

radians_from_degrees = math.pi / 180.0
degrees_from_radians = 1.0 / radians_from_degrees
half_pi = math.pi / 2.0

def __to_radians(degrees):
    return degrees * radians_from_degrees

def __to_degrees(radians):
    return radians * degrees_from_radians

def __get_hemisphere(zoom, pixel_tile_size):
    return pixel_tile_size * math.pow(2.0, zoom - 1.0)

def __to_pixel(semiarcs, hemisphere):
    return hemisphere * (1.0 + semiarcs)

def __to_x(lon, hemisphere):
    return __to_pixel(lon / 180.0, hemisphere)

def __to_y(lat, hemisphere):
    lat_radians = __to_radians(lat)
    f = min(max(math.sin(lat_radians), -0.9999), 0.9999)
    lat_radians = -0.5 * math.log((1 + f) / (1 - f))
    return __to_pixel(lat_radians / math.pi, hemisphere)

def to_pixel(lat, lon, zoom, pixel_tile_size = 256):
    hemisphere = __get_hemisphere(zoom, pixel_tile_size)
    return (
            __to_x(lon, hemisphere),
            __to_y(lat, hemisphere)
            )

def __to_semiarcs(pixels, hemisphere):
    return (pixels / hemisphere) - 1.0

def __to_lon(x, hemisphere):
    return __to_semiarcs(x, hemisphere) * 180.0

def __to_lat(y, hemisphere):
    y = -__to_semiarcs(y, hemisphere) * math.pi
    return __to_degrees((2 * math.atan(math.exp(y))) - half_pi)

def to_wgs84(x, y, zoom, pixel_tile_size = 256):
    hemisphere = __get_hemisphere(zoom, pixel_tile_size)
    return (
            __to_lat(y, hemisphere),
            __to_lon(x, hemisphere)
            )

def __tile_to_pixel(tile, pixel_tile_size):
    return tile * pixel_tile_size

def get_extent(tile_x, tile_y, zoom, pixel_tile_size = 256):
    top = __tile_to_pixel(tile_y, pixel_tile_size)
    left = __tile_to_pixel(tile_x, pixel_tile_size)
    bottom = __tile_to_pixel(tile_y + 1, pixel_tile_size)
    right = __tile_to_pixel(tile_x + 1, pixel_tile_size)
    north_east = to_wgs84(right, top, zoom, pixel_tile_size)
    south_west = to_wgs84(left, bottom, zoom, pixel_tile_size)
    return (
            north_east,
            south_west
            )
