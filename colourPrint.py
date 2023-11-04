# Colour print
# unavailable in cmd

# print(f'\033[7;32;40mOnly because you\'re so beautiful\033[0m')

"""
colourPrint is a module which provides a func which can print colourful texts.
\033[a;b;cmXXX\033[0m is a method to print colourful texts.
a: display method, 4 for underline, 7 for reversed colour, other numbers for highlight.
b: foreground colour,
    black red green yellow blue purple cyan white 30-37
c: background colour,
    black red green yellow blue purple cyan white 40-47
XXX: the text.
"""


def colourPrint(mode: int, f_colour: int, b_colour: int, text: str, end: str = '\n') -> None:
    """
    :param mode: 4 for underline, 7 for reversed colour, other numbers for highlight.
    :param f_colour: foreground colour, 30-37 for black, red, green, yellow, blue, purple, cyan and white.
    :param b_colour: background colour, 40-47 for black, red, green, yellow, blue, purple, cyan and white.
    :param text: the text.
    :param end: the end character.
    """
    print(f'\033[' + str(mode) + ';' + str(f_colour) + ';' + str(b_colour) + 'm' + text + '\033[0m', end=end)


if __name__ == '__main__':
    print("This program is", __file__, ', a module provides a colourful print func.')
    # __file__ variable can store the path of the file.
    help(colourPrint)
    colourPrint(7, 31, 40, 'Colourful', end='')
    colourPrint(7, 32, 40, 'Print!')
