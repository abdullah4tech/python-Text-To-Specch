# Import the gTTS library
from gtts import gTTS
import os

# Open the text file for reading (replace "your_text_file.txt" with the actual file path)
with open("your_text_file.txt", "r") as file:
    text = file.read()

# Create a gTTS object and convert the text to speech (English language, not slowed down)
speech = gTTS(text=text, lang='en', slow=False)

# Save the speech as an MP3 file (use try-except block for error handling)
try:
    speech.save("output_voice.mp3")
    print("File saved successfully")
except:
    print("Error saving the file")

# Play the generated voice file (on supported systems)
os.system("output_voice.mp3")  
