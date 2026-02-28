from llm.llm_service import generate_code


def build_strict_prompt():
    return """
You are a compiler.

Translate the Java code below into Python.

STRICT RULES:
- Output ONLY valid Python code.
- No explanations.
- No markdown.
- No comments.
- No docstrings.
- Do not modify logic.

Java code:
public int add(int a,int b){ return a+b; }
"""


if __name__ == "__main__":
    prompt = build_strict_prompt()

    print("Sending request to Ollama...\n")
    result = generate_code(prompt)

    print("=== Model Output ===\n")
    print(result.strip())