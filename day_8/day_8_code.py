"""
The image you received is 25 pixels wide and 6 pixels tall.

To make sure the image wasn't corrupted during transmission, the Elves would like you to find the layer that contains the fewest 0 digits. On that layer, what is the number of 1 digits multiplied by the number of 2 digits?
"""
file_path = "day_8/"
question_file = "day_8_input.txt"
with open(file_path + question_file) as f:
    lines = f.read()
length_of_layer = 25 * 6

layers = []

for i in range(0, int(len(lines) / length_of_layer)):
    partition = lines[length_of_layer * i: length_of_layer * (i+1)]
    layers.append(partition)

lowest_zeroes = float("inf")
lowest_zeroes_layer = -1
for index, layer in enumerate(layers):
    if layer.count("0") < lowest_zeroes:
        lowest_zeroes = layer.count("0")
        lowest_zeroes_layer = index

print(f'{layers[lowest_zeroes_layer].count("1") * layers[lowest_zeroes_layer].count("2")}')

pixel_print = ""
for pixel in range(0, len(layers[0])):
    pix_colour = "-"
    layer = 0
    while layers[layer][pixel] == "2":
        layer += 1
    pix_colour = str(layers[layer][pixel])
    if (pixel+1) % 25 == 0 and pixel != 0:
        pix_colour = pix_colour+"\n"
    pixel_print += pix_colour

"""
https://inventwithpython.com/bigbookpython/project57.html

Shows how to use the bar character to visualise things more clearly.
"""
print(pixel_print.replace("1", chr(9608)).replace("0", " "))