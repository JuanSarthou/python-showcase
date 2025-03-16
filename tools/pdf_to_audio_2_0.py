# Install necessary libraries
!pip install PyPDF2 gTTS pydub

# Import necessary libraries
import PyPDF2
from gtts import gTTS
from google.colab import files
from pydub import AudioSegment
from pydub.playback import play
from IPython.display import Audio
import re

# Step 1: Upload PDF file
uploaded = files.upload()

# Step 2: Read and preprocess the uploaded PDF
pdf_file = next(iter(uploaded))  # Get the uploaded file name dynamically while using colab

with open(pdf_file, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()

# Step 3: Preprocess text to remove unnecessary line breaks and spaces
# Replace multiple spaces with a single space
text = re.sub(r'\s+', ' ', text)

# Step 4: Convert extracted text to speech using gTTS
tts = gTTS(text, lang='en')

# Step 5: Save the initial audio file
audio_file = "output_audio.mp3"
tts.save(audio_file)

# Step 6: Use pydub to increase the speech speed
audio = AudioSegment.from_mp3(audio_file)
faster_audio = audio.speedup(playback_speed=1.2)  # Speed up by 20%

# Step 7: Export the modified audio
faster_audio_file = "faster_output_audio.mp3"
faster_audio.export(faster_audio_file, format="mp3")

# Step 8: Play audio in Colab (optional)
Audio(faster_audio_file)

# Step 9: Download the final audio file
files.download(faster_audio_file)
