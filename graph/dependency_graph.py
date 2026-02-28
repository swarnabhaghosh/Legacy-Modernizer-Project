import os
import javalang
import networkx as nx


def build_graph(repo_path):
    graph = nx.DiGraph()
    methods = {}

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".java"):
                path = os.path.join(root, file)

                with open(path, "r", encoding="utf-8") as f:
                    code = f.read()

                tree = javalang.parse.parse(code)

                for _, node in tree:
                    if isinstance(node, javalang.tree.MethodDeclaration):
                        method_id = f"{file}:{node.name}"
                        methods[method_id] = node
                        graph.add_node(method_id)

    for method_id, node in methods.items():
        for _, child in node:
            if isinstance(child, javalang.tree.MethodInvocation):
                called_name = child.member

                for other_id in methods:
                    if other_id.endswith(f":{called_name}"):
                        graph.add_edge(method_id, other_id)

    return graph