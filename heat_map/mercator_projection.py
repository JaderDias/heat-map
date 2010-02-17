import math

radians_to_degrees = math.pi / 180

def to_pixel(lat, lon, zoom, pixel_tile_size = 256):
    hemisphere_pixels = pixel_tile_size * math.pow(2, zoom - 1)
    degrees_to_pixels = hemisphere_pixels / 180
    radians_to_pixels = hemisphere_pixels / math.pi
    x = hemisphere_pixels + (lon * degrees_to_pixels)
    f = min(max(math.sin(lat * radians_to_degrees), -0.9999), 0.9999)
    y = hemisphere_pixels + (.5 * math.log((1 + f) / (1 - f)) * -radians_to_pixels)
    return (x, y);
