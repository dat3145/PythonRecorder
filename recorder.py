import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import pyaudio
import wave
import os
from robot.api import logger
import numpy as np


def record_sound(duration, id, name):
    fs = 44100
    seconds = int(duration)
    sd.default.device = int(id)
    
    sound_path = os.path.join(os.path.dirname(__file__),"sound")
    filename = "{name}_{id}.wav".format(name=name, id=id)
    filepath = os.path.join(sound_path, filename)
    logger.console("\nRecording at id %s" %id)
    
    try:
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()
        y = (np.iinfo(np.int32).max * (myrecording/np.abs(myrecording).max())).astype(np.int32)    
        write(filepath, fs, y)
        logger.console("Success at id %s" %id)
        return filepath
        
    except Exception as e:
        logger.console("Error at id {id} : {error}".format(id=id, error=e))
    
    
    
    
def convert_sound_to_text(sound):
    r = sr.Recognizer()
    with sr.AudioFile(sound) as source:
        # r.adjust_for_ambient_noise(source)
        logger.console("\nConverting Audio To Text ..... ")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        logger.console("Converted Audio Is : " + text)
        return text
    except Exception as e:
        logger.console("Error occured: {error}".format(error=e))
        
        
def show_devices():
    print sd.query_devices()
    for i in range(len(sd.query_devices())):
        logger.console(str(i) + " : " + str(sd.query_devices()[i]["name"]))



# show_devices()
# path = record_sound(5, 1)
# convert_sound_to_text(path)