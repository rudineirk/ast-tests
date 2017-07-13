from json import dumps

import tatsu
from tatsu.walkers import NodeWalker


class UmsgNodeWalker(NodeWalker):
    def walk_Start(self, nodes):
        values = {}
        for stmt in nodes.ast:
            stmt = self.walk(stmt)
            values[stmt[0]] = stmt[1]

        return values

    def walk_Assignment(self, node):
        var = self.walk(node.var)
        value = self.walk(node.value)
        return (var, value)

    def walk_Identifier(self, node):
        return node.ast

    def walk_BoolTrue(self, node):
        return True

    def walk_BoolFalse(self, node):
        return False

    def walk_Int(self, node):
        return int(node.ast)

    def walk_Float(self, node):
        return float(node.ast)

    def walk_String(self, node):
        return node.ast[1:-1]


def simple_parse():
    grammar = open('umsg.ebnf').read()
    code = open('example.umsg').read()

    parser = tatsu.compile(grammar, asmodel=True)
    ast = parser.parse(code)
    walker = UmsgNodeWalker()
    print(dumps(walker.walk(ast), indent=2))


def main():
    simple_parse()


if __name__ == '__main__':
    main()
