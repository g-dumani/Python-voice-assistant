import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commands import Commander
import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

#def echo(text):
#    subprocess.call('echo ' + text, shell=True)
running= True
def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()


r = sr.Recognizer()
cmd = Commander()

def initSpeech():
    print("Listening...")

    play_audio("audio_initiate.wav")

    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)

    play_audio("audio_end.wav")

    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't understand you, bro.")

    print("Your command:")
    print(command)
    if command in ["quit", "exit", "bye", "goodbye"]:
        global running
        running = False

    cmd.discover(command)

    #speak.Speak(command)





while running == True:
    initSpeech()
