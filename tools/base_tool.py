class BaseTool:
    def __init__(self, file, background: list = None, character: str = ' '):
        self.file = file
        self.character = character
        self.background = background if background else []
