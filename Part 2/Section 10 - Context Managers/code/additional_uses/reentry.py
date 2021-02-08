from redirect_std_out import OutToFile


class ListMaker:
    def __init__(self, title, prefix='-', indent=3) -> None:
        self._title = title
        self._prefix = prefix
        self._indent = indent
        self._current_indent = 0
        print(title)

    def __enter__(self):
        self._current_indent += self._indent
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self._current_indent -= self._indent
        return False

    def print_item(self, arg):
        s = ' ' * self._current_indent + self._prefix + str(arg)
        print(s)


with ListMaker(title='Items') as lm:
    lm.print_item('Item 1')
    with lm:
        lm.print_item('sub item 1a')
        lm.print_item('sub item 1b')
    lm.print_item('Item 2')
    with lm:
        lm.print_item('sub item 2a')
        lm.print_item('sub item 2b')


with OutToFile("list_maker.txt"):
    with ListMaker(title='Items') as lm:
        lm.print_item('Item 1')
    with lm:
        lm.print_item('sub item 1a')
        lm.print_item('sub item 1b')
    lm.print_item('Item 2')
    with lm:
        lm.print_item('sub item 2a')
        lm.print_item('sub item 2b')
