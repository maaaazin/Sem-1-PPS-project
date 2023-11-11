import streamlit as st

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}


def to_morse_code(message):
    morse_code = ''
    for char in message.upper():
        if char in morse_dict:
            morse_code += morse_dict[char] + ' '
    return morse_code

def from_morse_code(morse_code):
    message = ''
    morse_code = morse_code.split(' ')
    for code in morse_code:
        for char, morse in morse_dict.items():
            if morse == code:
                message += char
    return message

def main():
    st.title("Morse Code Converter")

    option = st.selectbox("Choose an option:", ["Convert text to Morse code", "Convert Morse code to text"])

    if option == "Convert text to Morse code":
        message = st.text_input("Enter a message to convert to Morse code:")
        if st.button("Convert"):
            morse_code = to_morse_code(message)
            st.write("Morse Code:", morse_code)

    elif option == "Convert Morse code to text":
        morse_code = st.text_input("Enter a Morse code sequence to convert to text:")
        if st.button("Convert"):
            message = from_morse_code(morse_code)
            st.write("Text:", message)


if __name__ == "__main__":
    main()
