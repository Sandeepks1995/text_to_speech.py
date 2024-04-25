import win32com.client as win32com

print("Welcome to Robospeaker 1.0. Created by Sandeep")
speak = win32com.Dispatch("SAPI.Spvoice")

text = "This is Text to speech python Program created by Sandeep Sharma. Using win32com.client. Enter what you want to speak"

speak.Speak(text)  # Use uppercase 'Speak' instead of 'speak'

while True:
    x = input("Enter what you want to speak (Enter '111' to exit from this programme): ")
    if x == "111":
        break
    speak.Speak(x)  # Use uppercase 'Speak' instead of 'speak'
