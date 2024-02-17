import sounddevice as sd
import time
from scipy.io import wavfile
import os
hztitle = 44100
sure = 10
print("Start Voice Recoder...")
recording = sd.rec(int(sure * hztitle), samplerate=hztitle, channels=2)
time.sleep(sure)
sd.stop()
print("Close.")
voicename = input("Enter the name of the folder where you want your audio file: ")
file_name = "recording.wav"
file_path = voicename + "/" + file_name
if not os.path.exists(voicename):
    os.mkdir(voicename)
wavfile.write(file_path, hztitle, recording)
print("Audo file", file_path, "saved to file address.")
exit()
