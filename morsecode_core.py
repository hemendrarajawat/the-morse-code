from morsecode_dict import MORSE_CODE_DICT

# This function takes the text message and returns the converted morse code.
def encrypt(message):
    if message == None:
        return None

    cipher = ''

    for letter in message:
        if letter in MORSE_CODE_DICT:
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += '# '

    return cipher.strip()


# This function takes the morse code cipher and returns the text message.
def decrypt(cipher):
    if cipher == None:
        return None

    message = ''

    for morse_letter in cipher.split(' '):
        if morse_letter in MORSE_CODE_DICT.values():
            message += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morse_letter)]
        else :
            message += '#'

    return message.strip().capitalize()
