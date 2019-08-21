from config import infile_path, outfile_path
from app import ToolRunner, read

instructions = \
'''C 20 4
L 1 2 6 2
L 6 3 6 4
R 16 1 20 3
B 10 3 o
'''
drawing = \
'''----------------------
|                    |
|                    |
|                    |
|                    |
----------------------
----------------------
|                    |
|xxxxxx              |
|                    |
|                    |
----------------------
----------------------
|                    |
|xxxxxx              |
|     x              |
|     x              |
----------------------
----------------------
|               xxxxx|
|xxxxxx         x   x|
|     x         xxxxx|
|     x              |
----------------------
----------------------
|oooooooooooooooxxxxx|
|xxxxxxooooooooox   x|
|     xoooooooooxxxxx|
|     xoooooooooooooo|
----------------------
'''


def create_file(file_path, write=''):
    file = open(file_path, 'w')
    file.write(write)
    file.close()


def test_match_template_and_file():
    create_file(infile_path, write=instructions)
    ToolRunner(
        outfile_path,
        read(infile_path)
    ).run()

    with open(outfile_path, 'r') as f:
        result = f.read()
    assert result == drawing


if __name__ == '__main__':
    test_match_template_and_file()
    print('Test was complited!')
