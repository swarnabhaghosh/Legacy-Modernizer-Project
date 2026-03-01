import os
import ast
from parser.base_parser import BaseParser


class PythonParser(BaseParser):

    def parse(self, repo_path):
        method_map = {}

        for root, _, files in os.walk(repo_path):
            for file in files:
                if file.endswith(".py"):
                    path = os.path.join(root, file)

                    try:
                        with open(path, "r", encoding="utf-8") as f:
                            code = f.read()

                        tree = ast.parse(code)

                        for node in ast.walk(tree):
                            if isinstance(node, ast.FunctionDef):
                                method_id = f"{file}:{node.name}"

                                method_map[method_id] = {
                                    "file": path,
                                    "method_name": node.name,
                                    "node": node
                                }

                    except Exception as e:
                        print(f"Parse error in {file}: {e}")

        return method_map