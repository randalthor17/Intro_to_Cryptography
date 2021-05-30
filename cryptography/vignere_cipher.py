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
        if ord(string[i]) >=65 and ord(string[i]) <= 90:
            char = chr((ord(string[i]) + ord(key[i])) % 26 + 65)
            ciphertext += char
        else:
            ciphertext += string[i]
    print('The encoded string is: ' + ciphertext)

def vignere_decode():
    string = input('Enter the string to be deciphered: ')
    string = string.upper()
    key = input('Enter the cipher key: ')
    key = generate_key(string, key)
    deciphertext = ''
    for i in range(len(string)):
        if ord(string[i]) >=65 and ord(string[i]) <= 90:
            char = chr((ord(string[i]) - ord(key[i]) + 26) % 26 + 65)
            deciphertext += char
        else:
            deciphertext += string[i]
    print('The decoded string is: ' + deciphertext)

def vignere():
    print('From Wikipedia: \n')
    print('"The Vigenère cipher (French pronunciation: ​[viʒnɛːʁ]) is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword. It employs a form of polyalphabetic substitution."\n')
    sel = input('Press 1 and enter to encrypt a string using Vignere cipher, and press 2 and enter to decrypt a string: ')
    if sel == '1':
        vignere_encode()
    elif sel == '2':
        vignere_decode()
