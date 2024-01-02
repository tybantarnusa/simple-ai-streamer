from gtts import gTTS
import soundfile as sf
import sounddevice as sd

def speak(text, config):
    lang = config["voice"]["language"]
    tts = gTTS(text, lang=lang)
    tts.save("voice.mp3")
    
    data, samplerate = sf.read("voice.mp3")

    sd.default.device = int(config["voice"]["device"])
    sd.play(data, samplerate)
    sd.wait()
