from openai import OpenAI
client = OpenAI()


def aud_text():
    audio_file = open("file.wav","rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file,
    response_format="text"
    )
    return transcript
