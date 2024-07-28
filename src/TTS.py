import threading
import pyttsx3
import sounddevice as sd
import soundfile as sf

import time
import os
import subprocess
from pydub import AudioSegment
from pydub.playback import play
import edge_tts

class TTS():
    
    voice = "id-ID-ArdiNeural"
    data = ""
    tts_cmd = f'edge-tts --voice "{voice}" --text "{data}" --write-media "output.mp3"'
    

    def run(self):
        pass

    def speak_v1(self, text): # Legacy TTS - Upgrade Systems soon!
        print("# Speaking")
        engine = pyttsx3.init()
        engine.save_to_file(text, "output.wav")
        engine.runAndWait()

        data, fs = sf.read("output.wav", dtype='float32')


        sd.play(data, fs, device=7)
        sd.wait()
        print("# Speech Finished!")
        time.sleep(0.25)


    async def speak_v2(self, text):
        print("# Synthisising")
        communicate = edge_tts.Communicate(text, self.voice)
        print("# Saving synth")
        await communicate.save("output.mp3")
        try:
            audio = AudioSegment.from_mp3("output.mp3")
        except Exception as e:
            print(f"Error loading MP3 file: {e}")
            return
        
        print("# Speaking")
        data, fs = sf.read("output.mp3", dtype='float32')



        sd.play(data, fs, device=8)
        sd.wait()
        
        print("# Speech Finished!")
        time.sleep(0.25)


    
