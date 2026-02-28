# import ollama
#
# MODEL_NAME = "deepseek-coder"
#
#
# def generate_code(prompt):
#     try:
#         response = ollama.generate(
#             model=MODEL_NAME,
#             prompt=prompt,
#             options={
#                 "temperature": 0.0,
#                 "stop": ["```", "Explanation", "Here is", "This Python"]
#             }
#         )
#
#         return response["response"]
#
#     except Exception as e:
#         return f"LLM Error: {str(e)}"

import ollama


def generate_code(prompt, model_name="deepseek-coder"):
    """
    Sends prompt to Ollama model and returns raw response text.
    """

    response = ollama.generate(
        model=model_name,
        prompt=prompt,
        options={
            "temperature": 0.0
        }
    )

    return response.get("response", "").strip()