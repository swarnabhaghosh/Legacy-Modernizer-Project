from parser.code_parser import parse_repo
from graph.dependency_graph import build_graph
from optimizer.context_optimizer import build_context
from llm.llm_service import generate_code
import re


# 🔥 Set this after benchmarking
BEST_MODEL = "codellama:7b"


def build_prompt(source_lang, target_lang, context):
    return f"""
You are a strict code translator.

Translate the following {source_lang} class into equivalent {target_lang}.

Rules:
- Preserve ALL methods.
- Preserve class structure.
- Preserve method calls.
- Do not rename methods.
- Do not add decorators.
- Do not simplify logic.
- Output ONLY raw {target_lang} code.

Source Code:
{context}
"""


def extract_code(text):
    match = re.search(r"```python(.*?)```", text, re.DOTALL)
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

    prompt = build_prompt("Java", "Python", context)

    raw_output = generate_code(prompt, model_name=BEST_MODEL)
    clean_output = extract_code(raw_output)

    return {
        "converted_code": clean_output,
        "related_methods": related,
        "files_used": files
    }


if __name__ == "__main__":

    result = run_modernization("test_repo", "Login.java:login")

    print("Related Methods:", result["related_methods"])
    print("Files Used:", result["files_used"])
    print("\n===== FINAL MODERNIZED CODE =====\n")
    print(result["converted_code"])