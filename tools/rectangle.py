from tools.base_tool import BaseTool
from tools.line import Line


class Rectangle(BaseTool):

    def make(self, x1, y1, x2, y2):

        if x1 > x2 or y1 > y2:
            raise Exception('To draw a rectangle the coordinates of the upper left corner (x1, y1)'
                            ' and the lower right corner (x2, y2) are required!')

        Line(file=self.file, character=self.character, background=self.background
             ).make(x1, y1, x1, y2)
        Line(file=self.file, character=self.character, background=self.background
             ).make(x2, y1, x2, y2)
        Line(file=self.file, character=self.character, background=self.background
             ).make(x1+1, y1, x2-1, y1)
        Line(file=self.file, character=self.character, background=self.background
             ).make(x1+1, y2, x2-1, y2)

        for i in range(len(self.background)):
            self.file.write(''.join(self.background[i]) + '\n')

        return self.background
