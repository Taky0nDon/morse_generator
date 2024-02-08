from conversions import text_to_morse_dict, morse_to_text

greeting = "Welcome to the Morse Code Generator!\nPlease choose one of the following options\n1. Convert text to morse code\n2. Convert morse code to text"
mode_prompt = "What would you like to do?: "

print(greeting)
mode_choice = input(mode_prompt)

if mode_choice not in ["1", "2"]:
    print("You did not choose a valid mode")
elif mode_choice == "1":
    appropriate_dict = text_to_morse_dict
    start, end = "text", "morse code"
    separator = " "
elif mode_choice == "2":
    appropriate_dict = morse_to_text
    start, end = "morse code", "text"
    separator = ""

converter_prompt = f"Enter your {start} to convert to {end} here: "

text_to_convert = input(converter_prompt).upper()
if mode_choice == "2":
    text_to_convert = text_to_convert.split()

result = "".join([f"{appropriate_dict[char]}{separator}" for char in text_to_convert])

print(f"Your morse code: {result}")
