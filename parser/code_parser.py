import os
import javalang


def parse_repo(repo_path):
    method_map = {}

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

                        method_map[method_id] = {
                            "file": path,
                            "method_name": node.name,
                            "node": node
                        }

    return method_map