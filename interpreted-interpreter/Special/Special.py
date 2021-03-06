from Tree.NilNode import nil_node

class Special:
    @staticmethod
    def eval_list(l, env):
        # this is here to avoid circular imports between Tree.ConsNode and Special.Regular
        from Tree.ConsNode import ConsNode

        if l.is_null():
            return nil_node
        else:
            return ConsNode(l.get_car().eval(env), Special.eval_list(l.get_cdr(), env))

    @staticmethod
    def append_lists(node1, node2):
        from Tree.ConsNode import ConsNode
        if node1.is_null():
            return node2
        else:
            return ConsNode(node1.get_car(), Special.append_lists(node1.get_cdr(), node2))

    @staticmethod
    def reverse(node):
        from Tree.ConsNode import ConsNode
        if node.is_null() or node == None:
            return nil_node
        else:
            return Special.append_lists(Special.reverse(node.get_cdr()), ConsNode( \
                    node.get_car(), nil_node))

    @staticmethod
    def eval_body(node, env):
        result = Special.eval_list(node, env)
        return Special.reverse(result).get_car()

    def print(self, node, i, p=True):
        raise Exception("this special form does not have a print method")
