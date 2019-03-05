from Tree.Node import Node

class ClosureNode(Node):
    def __init__(self, lambd, env):
        self.f = lambd
        self.env = env

    def is_procedure(self):
        return True
