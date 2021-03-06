from Tree.Node import Node

class IdentNode(Node):
    def __init__(self, n):
        self.name = n

    def get_name(self):
        return self.name

    def is_symbol(self):
        return True

    def print(self, i, p=False):
        # no indenting
        print(self.name, end="")

    def eval(self, env):
        return env.lookup(self)
