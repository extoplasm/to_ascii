from PIL import Image

class to_ascii():
    def __init__(self, im):
        self.img = Image.open(im).convert('L')
        self.px = self.img.load()
        self.width, self.height = self.img.size
        self.ascii_values = ['@', '#', 'M', '&', 'R', '$', 'C', 'I', ';', ':', '*', '^', '"', '`', ' ']
    def convert(self):
        for x in range(self.width):
            for y in range(self.height):
                if self.px[x,y] < 17:
                    print(self.ascii_values[0])
                elif self.px[x,y] < 34:
                    print(self.ascii_values[1])
                elif self.px[x,y] < 51:
                    print(self.ascii_values[2])
                elif self.px[x,y] < 68:
                    print(self.ascii_values[3])

to_ascii("./idle.gif").convert()
