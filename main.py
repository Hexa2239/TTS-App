from src import TTS
import sounddevice as sd
import soundfile as sf
import asyncio

tts_thread = TTS.TTS()

while True:
    what_u_want = input("TTS: ")
    asyncio.run(tts_thread.speak_v2(what_u_want))
