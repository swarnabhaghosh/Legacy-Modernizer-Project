import re
import ast
from llm.llm_service import generate_code


MODELS = [
    "deepseek-coder",
    "codellama:7b",
    "llama3:8b"
]


def extract_code(text):
    """
    Extract only Python code from LLM output.
    """

    # Remove markdown block
    match = re.search(r"```python(.*?)```", text, re.DOTALL)
    if match:
        return match.group(1).strip()

    # If no markdown, try to find first class/def
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith(("class ", "def ")):
            return "\n".join(lines[i:]).strip()

    return text.strip()


def is_valid_python(code):
    try:
        ast.parse(code)
        return True
    except:
        return False


def score_output(code, expected_methods):
    score = 0

    # Syntax check
    if is_valid_python(code):
        score += 2

    # Method preservation
    for method in expected_methods:
        method_name = method.split(":")[-1]
        if method_name in code:
            score += 1

    # Penalize decorators
    if "@" in code:
        score -= 1

    # Penalize heavy explanation words
    forbidden_words = ["Explanation", "Here is", "This Python"]
    for word in forbidden_words:
        if word in code:
            score -= 1

    return score


def evaluate_models(prompt, expected_methods):

    results = {}
    best_model = None
    best_score = -999

    for model in MODELS:
        raw_output = generate_code(prompt, model_name=model)
        clean_code = extract_code(raw_output)
        score = score_output(clean_code, expected_methods)

        results[model] = {
            "score": score,
            "code": clean_code
        }

        if score > best_score:
            best_score = score
            best_model = model

    return best_model, results