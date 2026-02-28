from parser.code_parser import parse_repo
from graph.dependency_graph import build_graph
import networkx as nx

repo_path = "test_repo"

# Step 1: Parse repo
method_map = parse_repo(repo_path)
print("Method Map Content:", method_map)

print("Parsed Methods:")
for m in method_map:
    print(m)

# Step 2: Build graph
graph = build_graph(method_map)

print("\nGraph Edges:")
for edge in graph.edges:
    print(edge)

# Step 3: Test BFS
start = list(method_map.keys())[0]
related = list(nx.bfs_tree(graph, start).nodes())

print("\nRelated to", start)
print(related)