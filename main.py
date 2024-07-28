from src import TTS
import sounddevice as sd
import soundfile as sf
import asyncio

speech_device = 0
hasInit = False

tts_thread = TTS.TTS()

while True:
    if hasInit == False:
        print("Input and Output Devices:\n" + str(sd.query_devices()))
        curDeviceInput = input("Select a device: ")
        tts_thread.device = curDeviceInput
        hasInit = True
    else:
        what_u_want = input("TTS: ")
        asyncio.run(tts_thread.speak_v2(what_u_want))
