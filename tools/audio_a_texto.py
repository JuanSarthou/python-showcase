
!pip install SpeechRecognition pydub
!apt-get install -y ffmpeg

import speech_recognition as sr
from pydub import AudioSegment
from google.colab import files


# Initialize the recognizer
recognizer = sr.Recognizer()

uploaded = files.upload()

# Convert OGG to WAV
audio = AudioSegment.from_ogg("xxxxx")
audio.export("converted.wav", format="wav")
audio_file = "converted.wav"

# Load the audio file
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)

    # Recognize the speech in the audio
    try:
        text = recognizer.recognize_google(audio_data, language='es-ES')
        print("Transcription: ", text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
