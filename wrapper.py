#!/usr/bin/python3

def align_text(words, width, align):
    """
    Receives a list of words and align them.

    :param words: The text to be indented
    :param width: Size of characters on the line
    :param align: Align type (left, justify)
    :return: A line of text aligned.
    """
    align_types = {
        'justify': ' '.join(words).ljust(width),
        'left': ' '.join(words),
    }

    return align_types.get(align)


def wrap(text, width, align='left'):
    """
    Text is converted to an iterable of strings, and
    divide into lines of the given width, and generate
    them. The lines are fully justified, except for the
    last line, and lines with a single word, which are
    left-justified.

    :param text: The text to be indented
    :param width: Size of characters on the line
    :param align: Align type (left, justify)
    :return: A list of lines wrapped on the width.

    >>> text = "This is an example of text justification."
    >>> '\n'.join(list(wrap(text, 16)))
    'This is an',
    'example of text',
    'justification. '
    """

    line = [] # List of words in current line.
    col = 0 # Starting column of next word added to line.
    words = text.split()

    for word in words:
        if line and col + len(word) > width:
            if len(line) == 1:
                yield align_text(words, width, align)
            else:
                # After n + 1 spaces are placed between each pair of
                # words, there are r spaces left over; these result in
                # wider spaces at the left.
                n, r = divmod(width - col + 1, len(line) - 1)
                narrow = ' ' * (n + 1) if align is 'justify' else ' '
                if r == 0:
                    yield narrow.join(line)
                else:
                    wide = ' ' * (n + 2) if align is 'justify' else ' '
                    yield wide.join(line[:r] + [narrow.join(line[r:])])
            line, col = [], 0
        line.append(word)
        col += len(word) + 1
    if line:
        yield align_text(line, width, align)


if __name__ == '__main__':
    text = """
    In the beginning God created the heavens and the earth. Now the earth was 
    formless and empty, darkness was over the surface of the deep, and the 
    Spirit of God was hovering over the waters.

    And God said, "Let there be light," and there was light. God saw that the 
    light was good, and he separated the light from the darkness. God called 
    the light "day," and the darkness he called "night." And there was evening,
    and there was morning - the first day.
    """

    wrapped_text = wrap(text, 40)
    print('\n'.join(list(wrapped_text)))

    print('\n----------------------------------------\n')

    justified_text = wrap(text, 40, 'justify')
    print('\n'.join(list(justified_text)))
