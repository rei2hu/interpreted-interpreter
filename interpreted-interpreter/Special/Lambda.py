from Special.Special import Special
from Tree.ClosureNode import ClosureNode

class Lambda(Special):
    def eval(self, node, env):
        return ClosureNode(node, env)

    def print(self, node, i, p=True):
        if not p:
            print()
            print("%s(" % (" " * i), end="")
        print("lambda ", end="")
        node.get_cdr().get_car().print(i + 4) # args list
        node.get_cdr().get_cdr().print(i + 4, True) # body
        if not p:
            print(")", end="")
