import toml
import youtube
import console

with open("config.toml", "r") as conf:
    config = toml.load(conf)

mode = config["system"]["mode"]

if mode == "youtube":
    youtube.run_youtube_mode(config)
elif mode == "console":
    console.run_console_mode(config)
else:
    print(f"Mode {mode} is not implemented.")
