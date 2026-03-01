import ollama


def generate_code(prompt, model_name="codellama:7b"):
    """
    Send prompt to Ollama and return raw response.
    """

    try:
        response = ollama.generate(
            model=model_name,
            prompt=prompt,
            options={
                "temperature": 0.0
            }
        )
        return response.get("response", "").strip()

    except Exception as e:
        print("LLM Error:", e)
        return ""