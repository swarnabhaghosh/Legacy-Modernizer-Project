import re
import os
import networkx as nx


def remove_comments(code):
    code = re.sub(r'//.*', '', code)
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    return code


def build_context(start_method_id, graph, method_map):
    related_methods = list(nx.bfs_tree(graph, start_method_id).nodes())

    required_files = set()
    for m in related_methods:
        required_files.add(method_map[m]["file"])

    context = ""

    for file_path in required_files:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                code = f.read()
                code = remove_comments(code)
                context += code + "\n\n"

    return context, related_methods, list(required_files)