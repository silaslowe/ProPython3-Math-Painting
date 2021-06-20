import numpy as np
from PIL import Image


# data = np.zeros((5, 4, 3), dtype=np.uint8)
# data[:] = [255, 255, 0]
#
# data[1:3, 1:3] = [255, 0, 0]

# img = Image.fromarray(data, 'RGB')
# img.save('canvas.png')


class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        pass


class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas[1:3, 1:4] = [255, 0, 0]
        img = Image.fromarray(canvas)
        return img


class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def make(self):
        data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        data[:] = self.color
        return data


new_canvas = Canvas(5, 4, [255, 255, 255])

add_rect = Rectangle(1, 1, 2, 3, [255, 0, 0])

new_canvas_rect = add_rect.draw(new_canvas)

add_square = new_canvas_rect.make('new_canvas2.png')

# img = Image.fromarray(data)
# img.save(image_path)


print(add_square)
