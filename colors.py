import colorgram

colors = colorgram.extract('landscape.jpg', 8)

final_colour = []
for _ in range(8):
    r = colors[_].rgb.r
    g = colors[_].rgb.g
    b = colors[_].rgb.b
    arr_color = (r, g, b)
    final_colour += arr_color

print(final_colour)
