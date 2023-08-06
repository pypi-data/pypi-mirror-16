# -*- coding: utf-8 -*-
import ast
from collections import Iterable


__version__ = '1.0.4'


mutable_types = [
    ast.Dict,
    ast.List,
    ast.Set,
]


class MutableDefaultChecker(object):
    """Mutable default argument checker.

    Flake8 extension that alerts when a mutable type is used
    as an argument's default value.
    """
    name = 'flake-mutable'
    version = __version__
    _error_tmpl = '{} - mutable default arg of type {}'
    _code = 'M511'

    def __init__(self, tree, filename):
        self.tree = tree

    def run(self):
        unexplored_nodes = self.tree.body
        while unexplored_nodes:
            node = unexplored_nodes.pop()
            if isinstance(node, ast.FunctionDef):
                for default in node.args.defaults:
                    if any([
                        isinstance(default, mutable_type)
                        for mutable_type in mutable_types
                    ]):
                        error_msg = self._error_tmpl.format(
                            self._code, type(default).__name__
                        )
                        yield node.lineno, 0, error_msg, type(self)
            if 'body' in node._fields:
                unexplored_nodes.extend(
                    node.body if isinstance(node.body, Iterable)
                    else [node.body]
                )
