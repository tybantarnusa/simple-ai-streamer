import voice
from brain import Brain

def run_console_mode(config):
    ai = Brain(config)
    chat_history = []

    while True:
        message = input("Chat: ")
        chat_history.append({
            "role": "user",
            "content": message,
        })

        prompt = ai.generate_prompt(chat_history)
        answer = ai.reply_chat(prompt)

        chat_history.append({
            "role": "assistant",
            "content": answer,
        })

        print(f"AI: {answer}")
        voice.speak(answer, config)

        if len(chat_history) > 5:
            chat_history.pop(0)
