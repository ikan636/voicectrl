#!/.venv/Scripts/python
import pyaudio
import wave
#import openai-stxt
FRMT = pyaudio.paInt16
CHNLS = 2
RATE = 44100
CHNK = 1024
RECORD_SECONDS = 7
WAVE_OUTPUT_FILENAME = "file.wav"
 
audio = pyaudio.PyAudio()
test = "test"
# start Recording
stream = audio.open(format=FRMT, channels=CHNLS,
                rate=RATE, input=True,
                frames_per_buffer=CHNK)
print("recording...")
frames = []
 
for i in range(0, int(RATE / CHNK * RECORD_SECONDS)):
    data = stream.read(CHNK)
    frames.append(data)
print("finished recording")
 
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHNLS)
waveFile.setsampwidth(audio.get_sample_size(FRMT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
