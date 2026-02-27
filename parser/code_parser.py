import os
import javalang

def parse_repo(repo_path):
    all_methods = {}
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".java"):
                path = os.path.join(root, file)
                with open(path, "r") as f:
                    code = f.read()
                tree = javalang.parse.parse(code)
                for _, node in tree:
                    if isinstance(node, javalang.tree.MethodDeclaration):
                        all_methods[node.name] = path
    return all_methods

if __name__ == "__main__":
    repo = "repo"
    methods = parse_repo(repo)
    print(methods)