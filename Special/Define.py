from Special.Special import Special
from Tree.NilNode import nil_node
from Tree.IdentNode import IdentNode

class Define(Special):
    def eval(self, node, env):
        from Tree.ConsNode import ConsNode
        if node.get_cdr().get_car().is_pair(): # function def
            params = node.get_cdr().get_car().get_cdr()
            fun_name = node.get_cdr().get_car().get_car()
            body = node.get_cdr().get_cdr()
            val = ConsNode(IdentNode("lambda"), ConsNode(params, body)).eval(env)
            env.define(fun_name, val)
        else: # normal def
            val = node.get_cdr().get_cdr().get_car().eval(env)
            ident = node.get_cdr().get_car()
            env.define(ident, val)
        return nil_node
