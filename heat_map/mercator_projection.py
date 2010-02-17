import math

radians_from_degrees = math.pi / 180

def __to_radians(degrees):
    return degrees * radians_from_degrees

def __to_pixel(radians, hemisphere):
    return hemisphere * (1 + (radians / math.pi))

def __to_x(lon_radians, hemisphere):
    return __to_pixel(lon_radians, hemisphere)

def __to_y(lat_radians, hemisphere):
    f = min(max(math.sin(lat_radians), -0.9999), 0.9999)
    y = -.5 * math.log((1 + f) / (1 - f))
    return __to_pixel(y, hemisphere)

def to_pixel(lat, lon, zoom, pixel_tile_size = 256):
    hemisphere = pixel_tile_size * math.pow(2, zoom - 1)
    (lat_radians, lon_radians) = map(__to_radians, (lat, lon))
    return (
            __to_x(lon_radians, hemisphere),
            __to_y(lat_radians, hemisphere)
            )
