
import whisper

model = whisper.load_model("base")

audio = r"Python\audiorag\data\Never gonna give you up.mp3"
result = model.transcribe(audio, fp16 = False)
print(result["text"])