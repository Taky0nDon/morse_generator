from conversions import text_to_morse_dict, morse_to_text

greeting = "Welcome to the Morse Code Generator!\
        Please choose one of the following options\
        1. Convert text to morse code\
        2. Convert morse code to text"
mode_prompt = "What would you like to do?: "
converter_prompt = "Enter your text to convert to morse code here: "

mode_choice = input(mode_prompt)

if mode_prompt not in ["1", "2"]:
    print("You did not choose a valid mode")
elif mode_prompt == "1":
    appropriate_dict = text_to_morse_dict
elif mode_prompt == "2":
    appropriate_dict = morse_to_text

text_to_convert = input(converter_prompt).upper()

result = "".join([f"{appropriate_dict[char]} " for char in text_to_convert])

print(f"Your morse code: {result}")
