import math

degrees_to_radians_ratio = 180 / math.pi;
radians_to_degrees_ratio = 1 / degrees_to_radians_ratio;

def to_pixel(lat, lon, zoom, pixel_tile_size = 256):
    hemisphere_pixels = pixel_tile_size * math.pow(2, zoom - 1)
    x_to_degrees_ratio = hemisphere_pixels / 180
    y_to_radians_ratio = hemisphere_pixels / math.pi
    x = hemisphere_pixels + (lon * x_to_degrees_ratio)
    f = min(max(math.sin(lat * radians_to_degrees_ratio), -0.9999), 0.9999)
    y = hemisphere_pixels + (.5 * math.log((1 + f) / (1 - f)) * -y_to_radians_ratio)
    return (x, y);
