def caeser(str, rot_val):
    str_new = ''
    str_lst = list(str)
    for char in str_lst:
        char_int = ord(char)
        if char_int >=65 and char_int <= 90:
            if char_int + rot_val > 90:
                char_int += rot_val - 26
            else:
                char_int += rot_val
        elif char_int >= 97 and char_int <= 122:
            if char_int + rot_val > 122:
                char_int += rot_val - 26
            else:
                char_int += rot_val
        char_new = chr(char_int)
        str_new += char_new
    return str_new

def caeser_encode():
    str = input('Enter the string to be caeser-ciphered: ')
    rot_val = int(input('Enter the shift count: '))
    str_conv = caeser(str, rot_val)
    print('The ciphered string is: ' + str_conv)

def caeser_decode():
    str = input('Enter the string to be deciphered: ')
    rot_val = input('Enter the shift count if it is known, or keep it blank to try all possible shift counts: ')
    if rot_val == '':
        print('Tring all values of shift count: \n')
        for rot_val in range(1, 26):
            print(caeser(str, rot_val))
        print()
        print('The one that makes sense should be the decoded string.')
    else:
        rot_val = 26 - int(rot_val)
        str_conv = caeser(str, rot_val)
        print('The deciphered string is: ' + str_conv)

def caeser_cipher():
    print('From Wikipedia:\n')
    print('"In cryptography, a Caesar cipher, also known as Caesar`s cipher, the shift cipher, Caesar`s code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence."\n')
    sel = input('Press 1 and press Enter to encode a string with Caeser Cipher, or Press 2 and press Enter to decode a string with Caeser Cipher: ')
    if sel == '1':
        caeser_encode()
    elif sel == '2':
        caeser_decode()