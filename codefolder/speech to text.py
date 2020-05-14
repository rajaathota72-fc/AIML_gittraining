# Fork the repository
# Record an audio file for 1 min and convert into .wav file
# upload the file into the folder in which the code is present
# Add the speechtotext line with your audio file
# Make the pull request once the above the steps are accomplished
# Also upload the text file generated from the conversion to the forked repository and make a pull request
import speech_recognition as sr
def speechtotext(AUDIO_FILE):
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)
        text = r.recognize_google(audio)
    try:
        print(text)
        file = open('textfinal', 'w')
        file.write(text)
        file.close()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service;{0}".format(e))
speechtotext("sample1.wav")
speechtotext("anu_audio.wav")
