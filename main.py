from morse_code_converter import MorseCodeConverter

if __name__ == "__main__":
    user_word = input('Enter word to be converted to morse code: \n')
    morse_code_converter = MorseCodeConverter()
    morse_code_converter.convert_string_to_morse(user_word)