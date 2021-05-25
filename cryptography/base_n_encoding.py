from base64 import *
from file_folder_chooser import file_chooser, folder_chooser
ENCODING = 'utf-8'

def base64_encode():
    string_binary = bytes(input('Enter the string to be encoded to base64: '), ENCODING)
    string_binary_conv = standard_b64encode(string_binary)
    string_conv = string_binary_conv.decode(ENCODING)
    print('The string, converted to base64, is: ')
    print(string_conv)

def base64_decode():
    string_binary = bytes(input('Enter the string to be decoded from base64: '), ENCODING)
    string_binary_conv = standard_b64decode(string_binary)
    string_conv = string_binary_conv.decode(ENCODING)
    print('The string, decoded from base64, is: ')
    print(string_conv)

def base64_encode_file():
    print('Choose the input file to be encoded to base64.')
    input_file_location = file_chooser()
    print('Choose the output folder: ')
    output_file_location = folder_chooser()
    output_file_location += '/' + input('Enter the name of the output file: ')
    with open(input_file_location, 'rb') as input_file:
        with open(output_file_location, 'wb') as output_file:
            encode(input_file, output_file)
    print('The binary data found on the input file has been encoded and stored in the output file.')

def base64_decode_file():
    print('Choose the input file to be decoded from base64.')
    input_file_location = file_chooser()
    print()
    print('Choose the output folder: ')
    output_file_location = folder_chooser()
    output_file_location += '/' + input('Enter the name of the output file: ')
    with open(input_file_location, 'rb') as input_file:
        with open(output_file_location, 'wb') as output_file:
            decode(input_file, output_file)
    print('The binary data found on the input file has been decoded and stored in the output file.')

#FIXME: tkinter window stays in the background

def base32_encode():
    string_binary = bytes(input('Enter the string to be encoded to base32: '), ENCODING)
    string_binary_conv = b32encode(string_binary)
    string_conv = string_binary_conv.decode(ENCODING)
    print('The string, encoded to base32, is: ')
    print(string_conv)

def base32_decode():
    string_binary = bytes(input('Enter the string to be decoded from base32: '), ENCODING)
    string_binary_conv = b32decode(string_binary, casefold=True)
    string_conv = string_binary_conv.decode(ENCODING)
    print('The string, decoded from base32, is: ')
    print(string_conv)

def base16_encode():
    string_binary = bytes(input('Enter the string to be encoded to base16: '), ENCODING)
    string_binary_conv = b16encode(string_binary)
    string_conv = string_binary_conv.decode(ENCODING)
    print('The string, encoded to base16, is: ')
    print(string_conv)

def base16_decode():
    string_binary = bytes(input('Enter the string to be decoded from base16: '), ENCODING)
    string_binary_conv = b16decode(string_binary, casefold=True)
    string_conv = string_binary_conv.decode(ENCODING)
    print('The string, decoded from base16, is: ')
    print(string_conv)

def ascii85_encode():
    string_binary = bytes(input('Enter the string to be encoded to base85/ascii85: '), ENCODING)
    string_binary_conv = a85encode(string_binary)
    string_conv = string_binary_conv.decode(ENCODING)
    print('The string, encoded to base85/ascii85, is: ')
    print(string_conv)

def ascii85_decode():
    string_binary = bytes(input('Enter the string to be decoded from base85/ascii85: '), ENCODING)
    string_binary_conv = a85decode(string_binary)
    string_conv = string_binary_conv.decode(ENCODING)
    print('The string, decoded from base85/ascii85, is: ')
    print(string_conv)
