from PIL import Image

image = Image.open('input_image.jpg')
data = image.load()

width, heigth = image.size

for i in xrange(1, width - 1):
    for j in xrange(1, heigth - 1):
        medias = list()

        for color in xrange(3):
            sum_of_neighbors = \
                    data[i - 1, j][color] + \
                    data[i + 1, j][color] + \
                    data[i, j - 1][color] + \
                    data[i, j + 1][color] + \
                    data[i - 1, j - 1][color] + \
                    data[j + 1, j - 1][color] + \
                    data[i + 1, j + 1][color] + \
                    data[i - 1, j + 1][color] + \
                    data[i, j][color]

            medias.append(sum_of_neighbors / 9)

        data[i, j] = medias[0], medias[1], medias[2]
        # media_pixel = media_r / 9, media_b / 9, media_g / 9

image.show()
# image.save("output_image.jpg", "JPEG")
