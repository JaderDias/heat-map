import math

degrees_to_radians_ratio = 180 / math.pi;
radians_to_degrees_ratio = 1 / degrees_to_radians_ratio;

def to_pixel(lat, lon, zoom, pixel_tile_size = 256):
    half_pixel_globe_size = pixel_tile_size * math.pow(2, zoom) / 2
    x_to_degrees_ratio = half_pixel_globe_size / 180
    y_to_radians_ratio = half_pixel_globe_size / math.pi
    x = half_pixel_globe_size + (lon * x_to_degrees_ratio)
    f = min(max(math.sin(lat * radians_to_degrees_ratio), -0.9999), 0.9999)
    y = half_pixel_globe_size + (.5 * math.log((1 + f) / (1 - f)) * -y_to_radians_ratio)
    return (x, y);
