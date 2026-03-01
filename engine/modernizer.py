from parser.code_parser import parse_repo
from graph.dependency_graph import build_graph
from optimizer.context_optimizer import build_context
from llm.llm_service import generate_code
import re


# Set after benchmarking
BEST_MODEL = "codellama:7b"


def build_prompt(source_lang, target_lang, context):
    return f"""
Translate this {source_lang} class to {target_lang}.

Rules:
1. Preserve all method names exactly.
2. Preserve method calls exactly.
3. Do not rename anything.
4. Do not add decorators.
5. Do not add comments.
6. Output only raw {target_lang} code.

{context}
"""


def extract_code(text):
    match = re.search(r"```(?:python)?(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()

    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith(("class ", "def ")):
            return "\n".join(lines[i:]).strip()

    return text.strip()


def run_modernization(repo_path, start_method_id):

    method_map = parse_repo(repo_path)
    graph = build_graph(repo_path)

    context, related, files = build_context(
        start_method_id,
        graph,
        method_map
    )

    total_methods = len(method_map)
    used_methods = len(related)

    reduction = 100 - (used_methods / total_methods) * 100

    prompt = build_prompt("Java", "Python", context)

    raw_output = generate_code(prompt, model_name=BEST_MODEL)
    clean_output = extract_code(raw_output)

    return {
        "converted_code": clean_output,
        "related_methods": related,
        "files_used": files,
        "context_reduction_percent": round(reduction, 2)
    }


if __name__ == "__main__":

    result = run_modernization("test_repo", "UserService.java:login")

    print("Related Methods:", result["related_methods"])
    print("Files Used:", result["files_used"])
    print("Context Reduction:", result["context_reduction_percent"], "%")
    print("\n===== FINAL MODERNIZED CODE =====\n")
    print(result["converted_code"])