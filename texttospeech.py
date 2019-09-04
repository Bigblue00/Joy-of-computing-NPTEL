import speech_recognition as sr 
AUDIO_FILE=("a.wav")

r=sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
	audio=r.record(source)

try :
	print("audio file contains "+ r.recognize_google(aduio))
except sr.UnknownValueError :
	print("google speech recognisation couldn't understand")
except sr.RequestError:
	print("couldn't get the resaults")