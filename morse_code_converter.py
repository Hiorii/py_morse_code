import json
from morse_code_sound_converter import MorseCodeSoundConverter

class MorseCodeConverter:
    def __init__(self):
        self.morse_alphabet = {}
        self.get_morse_json_data()
        self.morse_code_sound_converter = MorseCodeSoundConverter()

    def get_morse_json_data(self):
        with open('data/morse_code_data.json') as f:
            self.morse_alphabet = json.load(f)

    def convert_string_to_morse(self, word: str) -> str:
        if word:
            morse_code: str = ''
            for letter in word:
                morse_code += f'{self.morse_alphabet[letter]}' + ' '
            self.morse_code_sound_converter.convert_morse_code_to_audio(morse_code)
        return word