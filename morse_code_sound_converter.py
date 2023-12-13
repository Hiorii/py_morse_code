import pyaudio
import wave
import time

LONG_LETTER = '-'
SHORT_LETTER = '.'
SPACE_LETTER = ' '
class MorseCodeSoundConverter():
    def __init__(self):
        self.long_sound = 'assets/sounds/long.wav'
        self.short_sound = 'assets/sounds/short.wav'
        self.chunk = 1024

    def open_sound(self, sound_file):
        f = wave.open(sound_file, "rb")
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)
        data = f.readframes(self.chunk)
        while data:
            stream.write(data)
            data = f.readframes(self.chunk)

    def convert_morse_code_to_audio(self, morse_code_string: str):
        for letter in morse_code_string:
            if letter == LONG_LETTER:
                self.open_sound(self.long_sound)
            if letter == SHORT_LETTER:
                self.open_sound(self.short_sound)
            if letter == SPACE_LETTER:
                time.sleep(0.7)