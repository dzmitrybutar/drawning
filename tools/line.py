from tools.base_tool import BaseTool


class Line(BaseTool):

    def check_parameters(self, x1, y1, x2, y2):
        max_height = len(self.background[0]) - 1
        max_width = len(self.background) - 1

        if x1 > max_height or x2 > max_height or x1 < 0 or x2 < 0 \
                or y1 > max_width or y2 > max_width or y1 < 0 or y2 < 0:
            raise Exception('Not correct coordinates!')

        if x1 != x2 and y1 != y2:
            raise Exception('Only horizontal or vertical lines!')

    def make(self, x1, y1, x2, y2, write=False):
        self.check_parameters(x1, y1, x2, y2)

        if x1 == x2:
            for y in range(len(self.background)):
                for x in range(len(self.background[y1])):
                    if y1 <= y2 and y1 <= y <= y2:
                        self.background[y][x1] = self.character
                    if y2 <= y1 and y2 <= y <= y1:
                        self.background[y][x1] = self.character

        if y1 == y2:
            for x in range(len(self.background[y1])):
                if x1 <= x2 and x1 <= x <= x2:
                    self.background[y1][x] = self.character
                if x1 >= x2 and x2 <= x <= x1:
                    self.background[y1][x] = self.character

        if write:
            for i in range(len(self.background)):
                self.file.write(''.join(self.background[i]) + '\n')
        return self.background
