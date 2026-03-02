import ollama
import time


def generate_code(prompt, model_name="codellama:7b", temperature=0.3):
    """
    Send prompt to Ollama and return response + latency.
    """

    try:
        start_time = time.time()

        response = ollama.generate(
            model=model_name,
            prompt=prompt,
            options={
                "temperature": temperature
            }
        )

        end_time = time.time()
        latency = round(end_time - start_time, 2)

        return response.get("response", "").strip(), latency

    except Exception as e:
        print("LLM Error:", e)
        return "", 0