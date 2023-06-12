import pyperclip as clip
import sys
import re

def count_strip_tabs(list_item: str) -> tuple[int, str]:
    r""" count the tabs and strip a list item
    
    Given a Markdown list line, count its indentation level. Removes the tabs and the hyhen
    
    Args:
        list_item (str : Markdown list item
    
    Returns:
        tabs (int): number of tabs
        content (str): stripped down content

    Raises
        AnyError: Default error
    Examples:SyntaxError: multiple statements found while compiling a single statement
        >>> count_strip_tabs('\t\t- test')
        (2, 'test')

        >>> count_strip_tabs("- line test")
        (0, 'line test')
    """
    tabs = 0
    while list_item[0] == "\t":
        tabs += 1
        list_item = list_item[1:]

    content = list_item.lstrip("- ")
    return tabs, content

def outline_to_heading() -> None:
    r""" Convert an outline to heading

    Read the clipboard for a Markdown list, transform its indentation into headings. Avoiding h1 header

    Args:

    Returns:
        String containing the heading representation of the given outlie
    Raises
        AnyError: Default error
    Examples:
        >>> import pyperclip
        >>> outline = '- line 0 indent\n\t\t- line 1 indent\ncontent\n\tcontent indented'
        >>> pyperclip.copy(outline)
        >>> outline_to_heading()
        >>> output = pyperclip.paste()
        >>> print(repr(output))
        '### line 0 indent\n##### line 1 indent\ncontent\n\tcontent indented'

    Todo:
        - New features
            - handle different types of indent signs
    """
    rawData = clip.paste()
    outline = rawData.split("\n")
    heading = ""

    for line in outline:
        # check if line is a list element
        pattern = r'^\t*-.*'
        match = re.match(pattern, line)
        if match:
            tabs, content = count_strip_tabs(line)
            heading += "###" + ''.join(["#" for i in range(tabs)]) +f" {content}\n"

        else:
            heading += line
            heading += "\n"
    # remove extra \n 
    heading = heading[:-1]
    clip.copy(heading)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(outline_to_heading())