import pytchat
import voice
from brain import Brain

def run_youtube_mode(config):
    ai = Brain(config)
    chat_history = []

    video_id = config["youtube"]["video_id"]
    chat = pytchat.create(video_id=video_id)
    while chat.is_alive():
        for c in chat.get().sync_items():
            author = c.author.name
            message = c.message

            chat_history.append({
                "role": "user",
                "content": f"{author}: {message}",
            })

            print(f"{author}: {message}")

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
