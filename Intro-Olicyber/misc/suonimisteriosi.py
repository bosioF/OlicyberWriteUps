from pydub import AudioSegment
import numpy as np
import scipy.signal

def process_morse_signal(morse_signal, sample_rate, dot_duration=0.1):
    morse_pattern = []
    current_signal = None
    current_duration = 0

    for bit in morse_signal:
        if bit != current_signal:
            if current_signal is not None:
                morse_pattern.append((current_signal, current_duration))
            current_signal = bit
            current_duration = 1 / sample_rate
        else:
            current_duration += 1 / sample_rate

    morse_text = ""
    for signal, duration in morse_pattern:
        if signal:
            if duration < dot_duration * 1.5:
                morse_text += "."
            else:
                morse_text += "-"
        else:
            if duration > dot_duration * 1:
                morse_text += " "
            elif duration > dot_duration * 0.5:
                morse_text += "|"

    return morse_text

MORSE_CODE_DICT = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z", "-----": "0", ".----": "1", "..---": "2",
    "...--": "3", "....-": "4", ".....": "5", "-....": "6",
    "--...": "7", "---..": "8", "----.": "9"
}

audio = AudioSegment.from_wav("audio.wav")
samples = np.array(audio.get_array_of_samples())
sample_rate = audio.frame_rate
threshold = np.max(np.abs(samples)) * 0.5
filtered_signal = np.abs(samples) > threshold
morse_text = process_morse_signal(filtered_signal, sample_rate)

decoded_message = ""
for morse_letter in morse_text.split("|"):
    if morse_letter.strip():
        decoded_message += MORSE_CODE_DICT.get(morse_letter, "?")
    else:
        decoded_message += " "

print("Messaggio decodificato:", decoded_message)
