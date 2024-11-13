def encode(message, shift):
    message = message.lower()
    result = [None]*len(message)
    for i, letter in enumerate(message):
        if ord(letter) >= 97 and ord(letter) <= 122:
            letter = chr(ord(letter) + int(shift))
            while ord(letter) < 97:
                letter = chr(ord(letter) + 26)
            while ord(letter) > 122:
                letter = chr(ord(letter) - 26)
        result[i] = letter
    return ''.join(result)

def decode(message, shift):
    message = message.lower()
    result = [None]*len(message)
    for i, letter in enumerate(message):
        if ord(letter) >= 97 and ord(letter) <= 122:
            letter = chr(ord(letter) - int(shift))
            while ord(letter) < 97:
                letter = chr(ord(letter) + 26)
            while ord(letter) > 122:
                letter = chr(ord(letter) - 26)
        result[i] = letter
    return ''.join(result)