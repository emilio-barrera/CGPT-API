from env_reader import env_reader
import openai

class gpt_api:
    config = None

    def __init__(self) -> None:
        self.config = env_reader()
        openai.api_key = self.config.get_var('API_KEY')

    def get_key(self) -> str:
        return openai.api_key

    def ask_gpt(self, prompt: str) -> str:
        try:
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = [{
                    "role": 'user',
                    "content": prompt
                }],
            )
            result = [i['message']['content'] for i in response["choices"]]
            result = '\n'.join(result)

            return result

        except Exception as error:
            return "ChatGPT is not available: " + error