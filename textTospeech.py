from gtts import gTTS
import os

# Providing the text
input_text = "Hello, This is an acknowledgement of the receipt of the email."

# Setting a different language (for a different voice)
language = "bn"  # Bengali language code

# Passing to gTTS engine
voice = gTTS(text=input_text, lang=language, slow=False)

# Specify the path to save the audio file in the current directory
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo.mp3")

# Creating and saving the audio file in the same folder as the script
voice.save(file_path)

# Playing the file
os.system(f"start {file_path}")
