import os
import javalang

def parse_repo(repo_path):
    method_map = {}

    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".java"):
                path = os.path.join(root, file)

                with open(path, "r", encoding="utf-8") as f:
                    code = f.read()

                try:
                    tree = javalang.parse.parse(code)
                except:
                    continue  # skip broken files

                for path_tuple, node in tree:
                    if isinstance(node, javalang.tree.MethodDeclaration):

                        # Unique identifier (file + method)
                        unique_name = f"{file}:{node.name}"

                        method_map[unique_name] = {
                            "file": path,
                            "method_name": node.name,
                            "position": node.position,  # line number
                            "node": node
                        }

    return method_map