import json
from codecs import open
from pprint import pprint

import tatsu


def simple_parse():
    grammar = open('atom.ebnf').read()

    parser = tatsu.compile(grammar)
    ast = parser.parse('''
    teste = 1;
    alpha1='teste\\'';
    ''')

    print('# SIMPLE PARSE')
    print('# AST')
    pprint(ast, width=20, indent=4)

    print()

    print('# JSON')
    print(json.dumps(ast, indent=4))


def main():
    simple_parse()


if __name__ == '__main__':
    main()