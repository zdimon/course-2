class Myiter:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

# Example
if __name__ == '__main__':
    root = Myiter(0)
    root.add_child('hello')
    root.add_child('world')
    for ch in root:
        print(ch)
# Outputs hello world
