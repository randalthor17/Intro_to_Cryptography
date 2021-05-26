def atbash():
    print('From Wikipedia: \n')
    print('"Atbash (Hebrew: אתבש‎; also transliterated Atbaš) is a monoalphabetic substitution cipher originally used to encrypt the Hebrew alphabet. It can be modified for use with any known writing system with a standard collating order."\n')
    print('To be noted, Atbash ciphers are encrypted and decrypted using the same method.\n')
    str = input('Enter the string to be atbash-ciphered/deciphered: ')
    str_new = ''
    str_lst = list(str)
    for char in str_lst:
        char_int = ord(char)
        if char_int >=65 and char_int <= 90:
            char_int = 155 - char_int
        elif char_int >= 97 and char_int <= 122:
            char_int = 219 - char_int
        char_new = chr(char_int)
        str_new += char_new
    print('The ciphered/deciphered string is: ' + str_new)
