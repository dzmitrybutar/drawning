from tools.base_tool import BaseTool


class Canvas(BaseTool):

    def make(self, width, height):
        background = []

        if width < 0 or height < 0:
            raise Exception('Not correct coordinates!')

        background.append(['-']*(width+2))
        for h in range(height):
            background.append([' ']*width)
            background[h+1].insert(0, '|')
            background[h+1].insert(len(background[h+1]), '|')
        background.append(['-']*(width+2))

        for i in range(len(background)):
            self.file.write(''.join(background[i]) + '\n')

        return background
