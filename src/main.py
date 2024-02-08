from conversions import text_to_morse_dict

greeting = "Welcome to the Morse Code Generator!\
        Enter your text to convert to morse code here: "

text_to_convert = input(greeting).upper()
result = "".join([f"{text_to_morse_dict[char]} " for char in text_to_convert])

print(f"Your morse code: {result}")
