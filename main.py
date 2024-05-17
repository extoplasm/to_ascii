from PIL import Image
import sys

class to_ascii():
    def __init__(self, im):
        self.img = Image.open(im).convert('L')
        self.px = self.img.load()
        self.width, self.height = self.img.size
        self.ascii_values = ['@', '#', 'M', '&', 'R', '$', 'C', 'I', ';', ':', '*', '^', '"', '`', ' ']
    def convert(self):
        self.final = []
        # there must be a better way to do this
        for y in range(self.height):
            for x in range(self.width):
                if self.px[x,y] < 17:
                    self.final.append(self.ascii_values[0])
                elif self.px[x,y] < 34:
                    self.final.append(self.ascii_values[1])
                elif self.px[x,y] < 51:
                    self.final.append(self.ascii_values[2])
                elif self.px[x,y] < 68:
                    self.final.append(self.ascii_values[3])
                elif self.px[x,y] < 85:
                    self.final.append(self.ascii_values[4])
                elif self.px[x,y] < 102:
                    self.final.append(self.ascii_values[5])
                elif self.px[x,y] < 119:
                    self.final.append(self.ascii_values[6])
                elif self.px[x,y] < 136:
                    self.final.append(self.ascii_values[7])
                elif self.px[x,y] < 153:
                    self.final.append(self.ascii_values[8])
                elif self.px[x,y] < 170:
                    self.final.append(self.ascii_values[9])
                elif self.px[x,y] < 187:
                    self.final.append(self.ascii_values[10])
                elif self.px[x,y] < 204:
                    self.final.append(self.ascii_values[11])
                elif self.px[x,y] < 221:
                    self.final.append(self.ascii_values[12])
                elif self.px[x,y] < 238:
                    self.final.append(self.ascii_values[13])
                else:
                    self.final.append(self.ascii_values[14])
            self.final.append('\n')
        return ''.join(self.final)


print(to_ascii(sys.argv[1]).convert())
