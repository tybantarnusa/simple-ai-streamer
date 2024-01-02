import requests

class Brain:
    def __init__(self, config):
        self.api_key = config["system"]["openai_api_key"]
        self.system_prompt = config["system"]["system_prompt"]

    def generate_prompt(self, chat_history):
        base_prompt = [
            {
                "role": "system",
                "content": self.system_prompt,
            }
        ]

        return base_prompt + chat_history
            

    def reply_chat(self, prompt):
        result = requests.post("https://api.openai.com/v1/chat/completions", json={
            "model": "gpt-3.5-turbo",
            "messages": prompt,
            "max_tokens": 175,
            "temperature": 1,
            "n": 1,
            "presence_penalty": 0.5,
        }, headers={"Authorization": f"Bearer {self.api_key}"})
        
        result_content = result.json()["choices"][0]["message"]["content"]

        return result_content
