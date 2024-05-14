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
                elif self.px[x,y] < 85:
                    print(self.ascii_values[4])
                elif self.px[x,y] < 102:
                    print(self.ascii_values[5])
                elif self.px[x,y] < 119:
                    print(self.ascii_values[6])
                elif self.px[x,y] < 136:
                    print(self.ascii_values[7])
                elif self.px[x,y] < 153:
                    print(self.ascii_values[8])
                elif self.px[x,y] < 170:
                    print(self.ascii_values[9])
                elif self.px[x,y] < 187:
                    print(self.ascii_values[10])
                elif self.px[x,y] < 204:
                    print(self.ascii_values[11])
                elif self.px[x,y] < 221:
                    print(self.ascii_values[12])
                elif self.px[x,y] < 238:
                    print(self.ascii_values[13])
                else:
                    print(self.ascii_values[14])

to_ascii("./idle.gif").convert()
