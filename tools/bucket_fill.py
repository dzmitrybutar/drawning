from tools.base_tool import BaseTool


class BucketFill(BaseTool):

    def check_parameters(self, x, y):
        max_height = len(self.background[0]) - 1
        max_width = len(self.background) - 1

        if self.background[y][x] != ' ':
            raise Exception('For flood fill only empty area!')

        if x > max_height or x < 0 or y > max_width or y < 0:
            raise Exception('Not correct coordinates!')

    def flood_fill(self, x, y, c):
        self.character = c
        maxw = len(self.background)
        maxh = len(self.background[0])

        if self.background[y][x] != ' ':
            return
        self.background[y][x] = self.character

        if x > 0:
            self.flood_fill(x - 1, y, c)
        if y > 0:
            self.flood_fill(x, y - 1, c)
        if x < maxh - 1:
            self.flood_fill(x + 1, y, c)
        if y < maxw - 1:
            self.flood_fill(x, y + 1, c)

    def make(self, x, y, c):
        self.check_parameters(x, y)
        self.flood_fill(x, y, c)
        for i in range(len(self.background)):
            self.file.write(''.join(self.background[i]) + '\n')
