
class TreeUtils(object):
    def __init__(self,root=None):
        self.root = root

    def print_tree(self):
        if self.root is None:
            return
        print(self.root.value)
        self.print_tree(self.root.left)
        self.print_tree(self.root.right)

class TreeFactory(object):