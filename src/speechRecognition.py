"""
Project: PopCornAgent
Name: speechRecognition.py
Authors: mikirubio & sgalella
Description: recognize speech from input
"""

import speech_recognition as sr

# Create a recognizer instance
def speechRecognizer():
    r = sr.Recognizer()
    mic = sr.Microphone()
    #sr.Microphone.list_microphone_names()
    with mic as source:
        audio = r.listen(source)
    audio_detected = r.recognize_google(audio)
    return audio_detected