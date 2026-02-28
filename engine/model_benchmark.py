from parser.code_parser import parse_repo
from graph.dependency_graph import build_graph
from optimizer.context_optimizer import build_context
from llm.llm_evaluator import evaluate_models


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


if __name__ == "__main__":

    repo = "test_repo"
    start_method = "Login.java:login"

    method_map = parse_repo(repo)
    graph = build_graph(repo)

    context, related, files = build_context(
        start_method,
        graph,
        method_map
    )

    prompt = build_prompt("Java", "Python", context)

    best_model, results = evaluate_models(prompt, related)

    print("\n===== MODEL BENCHMARK RESULTS =====\n")

    for model in results:
        print(f"{model} → Score: {results[model]['score']}")

    print("\nBest Model:", best_model)
    print("\nBest Model Output:\n")
    print(results[best_model]["code"])