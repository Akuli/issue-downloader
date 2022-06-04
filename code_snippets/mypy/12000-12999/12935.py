import mypy.main as MAIN
import mypy.build as BUILD

from mypy.nodes import SymbolTableNode, Node, NodeVisitor
py_file = "src/script_name"

mod = py_file.replace("/", ".")

files, opt = MAIN.process_options([f"{py_file}.py"])
opt.preserve_asts = True
opt.fine_grained_incremental = True
result = BUILD.build(files, options=opt)
tree = result.graph[mod].tree
names = tree.names.keys()

def is_node(value):
    return isinstance(value, Node) or isinstance(value, SymbolTableNode)

class MyVisitor(NodeVisitor):
    def generic_visit(self, node):
        print(f'entering {node.__class__.__name__}')
        if hasattr(node, "line"):
            print(f"\t{node.line}")
        if hasattr(node, "column"):
            print(f"\t{node.column}")
            if node.column == -1:
                return
        if hasattr(node, "name"):
            print(f"\t{node.name}")
        if not hasattr(node, "__mypyc_attrs__"):
            return
        node_fields = zip(
            node.__mypyc_attrs__,
            [
                getattr(node, attr)
                for attr in node.__mypyc_attrs__
            ]
        )
        for attr, value in node_fields:
            if isinstance(value, list):
                for v in value:
                    if not is_node(v):
                        continue
                    self.generic_visit(v)
            if is_node(value):
                #self.visit(value)
                self.generic_visit(value)

for name in names:
    symbol_table_node = tree.names[name]
    if symbol_table_node is None:
        continue
    visitor = MyVisitor()
    visitor.generic_visit(symbol_table_node.node)
