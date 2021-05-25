def atbash():
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
