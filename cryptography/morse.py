import csv

def csv_to_dict(csv_file):
    d = dict()
    with open(csv_file, "r") as f:
        csvread = csv.reader(f)
        next(csvread)
        for row in csvread:
            key = row[0]
            val = row[1]
            d[key] = val
    return d

def check_symbols_encode(char):
    if char == '&':
        char = 'Ampersand'
    elif char == "'":
        char = 'Apostrophe'
    elif char == '@':
        char = 'At sign'
    elif char == ')':
        char = 'Bracket close (parenthesis)'
    elif char == '(':
        char = 'Bracket open (parenthesis)'
    elif char == ':':
        char = 'Colon'
    elif char == ',':
        char = "Comma"
    elif char == '=':
        char = 'Equals sign'
    elif char == '!':
        char = 'Exclamation mark'
    elif char == '.':
        char = 'Full-stop (period)'
    elif char == '-':
        char = 'Hyphen'
    elif char == '*' or char == '×':
        char = 'Multiplication sign'
    elif char == '%':
        char = 'Percentage'
    elif char == '+':
        char = 'Plus sign'
    elif char == '"':
        char = 'Quotation marks'
    elif char == '?':
        char = 'Question mark (query)'
    elif char == '/':
        char = 'Slash'
    return char

def check_symbols_decode(char):
    if char == 'Ampersand':
        char = '&'
    elif char == 'Apostrophe':
        char = "'"
    elif char == 'At sign':
        char = '@'
    elif char == 'Bracket close (parenthesis)':
        char = ')'
    elif char == 'Bracket open (parenthesis)':
        char = '('
    elif char == 'Colon':
        char = ':'
    elif char == "Comma":
        char = ','
    elif char == 'Equals sign':
        char = '='
    elif char == 'Exclamation mark':
        char = '!'
    elif char == 'Full-stop (period)':
        char = '.'
    elif char == 'Hyphen':
        char = '-'
    elif char == 'Multiplication sign':
        char = '*'
    elif char == 'Percentage':
        char = '%'
    elif char == 'Plus sign':
        char = '+'
    elif char == 'Quotation marks':
        char = '"'
    elif char == 'Question mark (query)':
        char = '?'
    elif char == 'Slash':
        char = '/'
    return char

def morse_encode():
    string = input('Enter the text to be encoded into morse code: ')
    string = string.upper()
    morse = ''
    morse_dict = csv_to_dict('morse.csv')
    for char in string:
        char = check_symbols_encode(char)
        if char != ' ':
            print(char)
            morse += morse_dict[char] + ' '
        else:
            morse += '  '
    print('The morse code is: ' + morse)

def morse_decode():
    morse = input('Enter the morse code to be decoded: ') + ' '
    string = ''
    letter = ''
    morse_dict = csv_to_dict('morse.csv')
    for dot_dash in morse:
        if dot_dash != ' ':
            space = 0
            letter += dot_dash
        else:
            space += 1
            if space == 2:
                string += ' '
            else:
                if letter in morse_dict.values():
                    morse_list = list(morse_dict.values())
                    i = morse_list.index(letter)
                    char_list = list(morse_dict.keys())
                    char = char_list[i]
                    string += check_symbols_decode(char)
                    letter = ''
    print('The intended message is: ' + string)
