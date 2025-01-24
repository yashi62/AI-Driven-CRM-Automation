import openai

class AIEngine:
    def __init__(self):
        openai.api_key = 'YOUR_OPENAI_API_KEY'

    def generate_response(self, user_input):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"User: {user_input}\nAI:",
                max_tokens=150
            )
            return response.choices[0].text.strip()
        except Exception as e:
            raise RuntimeError(f"Error generating response: {e}")
