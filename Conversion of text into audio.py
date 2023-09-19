import pyttsx3
import time
import os

# Initialize the engine
engine = pyttsx3.init()

# Define a function for converting text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Set properties
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.8)  # Volume 0-1

# Get user input for the text to be converted
text = input("Enter the text you want to convert to audio: ")

# Convert the text to speech
print("Converting text to speech...")
speak(text)

# Save the converted audio file
filename = input("Enter the filename to save the audio as: ")
print(f"Saving audio to {filename}...")
engine.save_to_file(text, filename)
engine.runAndWait()
print("Audio saved successfully!")

# Play the audio file
play_audio = input("Do you want to play the audio file? (y/n): ")
if play_audio == 'y':
    print("Playing audio...")
    os.system(f"start {filename}")
    time.sleep(3)   # Wait for the audio to finish playing
else:
    print("Exiting program...")

# Shutdown the engine
engine.stop()
