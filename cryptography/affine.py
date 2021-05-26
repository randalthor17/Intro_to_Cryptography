def affine_encode():
    print('From Wikipedia: \n')
    print('"The affine cipher is a type of monoalphabetic substitution cipher, where each letter in an alphabet is mapped to its numeric equivalent, encrypted using a simple mathematical function, and converted back to a letter. The formula used means that each letter encrypts to one other letter, and back again, meaning the cipher is essentially a standard substitution cipher with a rule governing which letter goes to which. As such, it has the weaknesses of all substitution ciphers. Each letter is enciphered with the function (ax + b) mod 26, where b is the magnitude of the shift."\n')
    print('At this moment, this program only supports encryption using affine cipher.\n')
    allowed_a_vals = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    m = 26
    str_new = ''
    string = input('Enter the string to be encoded with affine cipher: ')
    a = int(input('Enter the value of encryption key a: '))
    while a not in allowed_a_vals:
        print('This value is not allowed. Allowed values of a are coprimes of ' + str(m) + ', namely ' + str(allowed_a_vals))
        a = int(input('Enter the value of encryption key a: '))
    b = int(input('Enter the value of encryption key b: '))
    str_lst = list(string)
    for char in str_lst:
        char_int = ord(char)
        if char_int >=65 and char_int <= 90:
            char_int = (a*(char_int -65)+b)%m + 65
        elif char_int >= 97 and char_int <= 122:
            char_int = (a*(char_int -97)+b)%m + 97
        char_new = chr(char_int)
        str_new += char_new
    print('The encoded string is: ' + str_new)
