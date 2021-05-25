def affine_encode():
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
