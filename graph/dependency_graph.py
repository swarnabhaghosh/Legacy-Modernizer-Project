import os
import json
import javalang
import networkx as nx

def build_graph(repo_path):
    graph = nx.DiGraph()
    methods = {}
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".java"):
                path = os.path.join(root, file)
                with open(path, "r") as f:
                    code = f.read()
                tree = javalang.parse.parse(code)
                for _, node in tree:
                    if isinstance(node, javalang.tree.MethodDeclaration):
                        methods[node.name] = node
                        graph.add_node(node.name)

    for name, node in methods.items():
        for _, child in node:
            if isinstance(child, javalang.tree.MethodInvocation):
                called = child.member
                if called in methods:
                    graph.add_edge(name, called)
    return graph

def save_json(graph):
    data = {}
    for node in graph.nodes:
        data[node] = list(graph.neighbors(node))
    with open("graph.json", "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    repo = "repo"
    graph = build_graph(repo)
    save_json(graph)
    print("Graph saved to graph.json")