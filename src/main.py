DIT = "."
DAH = "-"

greeting = "Welcome to the Morse Code Generator!\
        Enter your text to convert to morse code here: "
text_to_morse_dict = {
        " ": " / ",
        "?": "..--..",
        "!": "-.-.--",
        ".": ".-.-.-",
        "$": "...-..-",

        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": ".--",
        "Y": "-.--",
        "Z": "--..",

        "1":".----",
        "2":"..---",
        "3":"...--",
        "4":"....-",
        "5":".....",
        "6":"-....",
        "7":"--...",
        "8":"---..",
        "9":"----.",
        "0":"-----",
        }

text_to_convert = input(greeting)

result = ""
for char in text_to_convert:
    if char.isalpha():
        result += text_to_morse_dict[char.upper()] + " "
    else:
        result += f"{text_to_morse_dict[char]} "

print(f"Your morse code: {result}")
