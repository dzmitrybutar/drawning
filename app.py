from tools.canvas import Canvas
from tools.line import Line
from tools.rectangle import Rectangle
from tools.bucket_fill import BucketFill
from config import infile_path, outfile_path


def read(infile_path):
    with open(infile_path, 'r') as f:
        return f.read().splitlines()


class ToolRunner:
    def __init__(self, file_path, instructions):
        self.file_path = file_path
        self.instructions = instructions

    def check_errors(self):

        for instruction in self.instructions:
            instruction_type = instruction[0].lower()
            if instruction_type not in ['c', 'l', 'r', 'b']:
                raise Exception('Instruction ' + instruction[0].upper() + ' are not supported!')

        if not self.instructions:
            raise Exception('Add list of instructions!')

        if self.instructions[0].split()[0].lower() != 'c':
            raise Exception('You forgot to create a canvas!')

    def run(self):
        self.check_errors()

        with open(self.file_path, 'a') as f:
            template = []
            for instruction in self.instructions:
                instruction = instruction.split()
                instruction_type = instruction[0].lower()
                instruction_args = []
                for arg in instruction[1:]:
                    if arg.isdigit():
                        instruction_args.append(int(arg))
                    else:
                        instruction_args.append(arg)

                if instruction_type == 'c':
                    template = Canvas(f).make(*instruction_args)

                if instruction_type == 'l':
                    template = Line(f, background=template, character='x'
                                    ).make(*instruction_args, write=True)

                if instruction_type == 'r':
                    template = Rectangle(f, background=template, character='x'
                                         ).make(*instruction_args)

                if instruction_type == 'b':
                    BucketFill(f, background=template
                               ).make(*instruction_args)


if __name__ == '__main__':
    ToolRunner(outfile_path, read(infile_path)).run()
    print('The operation was successful! Check the output file!')
