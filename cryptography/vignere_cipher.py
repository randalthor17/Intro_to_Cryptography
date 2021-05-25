def generate_key(string, key):
    key = list(key)
    new_key = ''
    while len(string) > len(new_key):
        for i in range(len(key)):
            if len(string) > len(new_key):
                new_key += key[i]
    return new_key.upper()

def vignere_encode():
    string = input('Enter the string to be vignere-ciphered: ')
    string = string.upper()
    key = input('Enter the cipher key: ')
    key = generate_key(string, key)
    ciphertext = ''
    for i in range(len(string)):
        char = chr((ord(string[i]) + ord(key[i])) % 26 + 65)
        ciphertext += char
    print('The encoded string is: ' + ciphertext)

def vignere_decode():
    string = input('Enter the string to be deciphered: ')
    string = string.upper()
    key = input('Enter the cipher key: ')
    key = generate_key(string, key)
    deciphertext = ''
    for i in range(len(string)):
        char = chr((ord(string[i]) - ord(key[i]) + 26) % 26 + 65)
        deciphertext += char
    print('The decoded string is: ' + deciphertext)

