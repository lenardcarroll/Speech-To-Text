import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)  # Using Google Speech Recognition
    print("Audio-to-Text:", text)
except sr.UnknownValueError:
    print("Speech recognition could not understand your audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
