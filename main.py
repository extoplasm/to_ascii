from PIL import Image

class to_ascii():
    def __init__(self, im):
        self.img = Image.open(im).convert('L')
        self.px = self.img.load()
        self.width, self.height = self.img.size
    def convert(self):
        for x in range(self.width):
            for y in range(self.height):
                print(self.px[x,y])

to_ascii("./idle.gif").convert()
