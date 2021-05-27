from cryptography.morse import morse_decode, morse_encode
from cryptography.freq_analysis import freq_analysis
from cryptography.hash import *
from cryptography.base_n_conversion import *
from cryptography.vignere_cipher import *
from cryptography.affine import *
from cryptography.caeser import *
from cryptography.atbash import *
from cryptography.base_n_encoding import *
from os import system, name


def main():
    with open('intro.txt', 'r') as intro:
        for line in intro:
            print(line)
    input('Press Enter to continue: ')
    clear()
    print('From Wikipedia:\n')
    print('"Cryptography, or cryptology (from Ancient Greek: κρυπτός, romanized: kryptós "hidden, secret"; and γράφειν graphein, "to write", or -λογία -logia, "study", respectively), is the practice and study of techniques for secure communication in the presence of third parties called adversaries. More generally, cryptography is about constructing and analyzing protocols that prevent third parties or the public from reading private messages; various aspects in information security such as data confidentiality, data integrity, authentication, and non-repudiation are central to modern cryptography. Modern cryptography exists at the intersection of the disciplines of mathematics, computer science, electrical engineering, communication science, and physics. Applications of cryptography include electronic commerce, chip-based payment cards, digital currencies, computer passwords, and military communications."\n\n')
    print('This is a collection of programs that demonstrate basics of cryptography. At the moment, this program supports encrypting and decrypting text strings with Atbash, Caeser and Vignere ciphers, encrypting text strings with Affine cipher, frequency analysis of strings, BASE16, BASE32, BASE64 and ASCII85 encoding and decoding, BASE64 encoding and decoding files, converting base-10 integers to base-n numbers and vice versa, converting strings to Morse code and vice versa and hashing files and strings into MD5, SHA-1, SHA-256, SHA-512, SHA3-256 and SHA3-512.')
    input('Press Enter to continue: ')
    clear()
    selection_menu_home()


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def selection_menu_home():
    print('This program is divided into 4 sections: \n')
    print('1. Ciphers,\n')
    print('2. Encoding/Decoding,\n')
    print('3. Base-n Conversion, and\n')
    print('4. Hashing.\n')
    print('Also as a bonus, there are 2 extra functions: \n')
    print('a. Morse code conersion, and\n')
    print('b. Frequency Distribution.\n')
    sel = input('Press 1/2/3/4/a/b and press Enter, or press 0 to exit the program: ')
    clear()
    if sel == '1':
        selection_ciphers()
    elif sel == '2':
        selection_encode_decode()
    elif sel == '3':
        selection_base_n()
    elif sel == '4':
        selection_hashing()
    elif sel == 'a':
        bonus_morse_convert()
    elif sel == 'b':
        bonus_freq_analysis()
    elif sel == '0':
        exit()
        
        

def selection_ciphers():
    print('From Wikipedia:\n')
    print('"In cryptography, a cipher (or cypher) is an algorithm for performing encryption or decryption—a series of well-defined steps that can be followed as a procedure. An alternative, less common term is encipherment. To encipher or encode is to convert information into cipher or code. In common parlance, "cipher" is synonymous with "code", as they are both a set of steps that encrypt a message; however, the concepts are distinct in cryptography, especially classical cryptography."\n')
    print('In this program, these ciphers have been implemented:\n')
    print('1. Atbash Cipher (Encrypting+Decrypting)\n')
    print('2. Caeser Cipher (Encrypting+Decrypting)\n')
    print('3. Affine Cipher (Encrypting Only)\n')
    print('4. Vignere Cipher (Encrypting+Decrypting)\n')
    sel = input('Press 1/2/3/4 and press Enter, or 0 and press Enter to go back to the main menu: ')
    clear()
    if sel == '1':
        atbash()
    elif sel == '2':
        caeser_cipher()
    elif sel == '3':
        affine_encode()
    elif sel == '4':
        vignere()
    elif sel == '0':
        selection_menu_home()
    sel = input('Press s and enter to go back to the cipher selection menu and press 0 and enter to go back to the main menu: ')
    clear()
    if sel == 's':
        selection_ciphers()
    elif sel == '0':
        selection_menu_home()

def selection_encode_decode():
    print('From wikipedia: \n')
    print('"A binary-to-text encoding is encoding of data in plain text. More precisely, it is an encoding of binary data in a sequence of printable characters. These encodings are necessary for transmission of data when the channel does not allow binary data (such as email or NNTP) or is not 8-bit clean."\n')   
    print('In this program, these encoding schemes have been implemented:\n')
    print('1. Base64 Encoding')
    print('2. Base64  Decoding')
    print('3. Base32 Encoding')
    print('4. Base32 Decoding')
    print('5. Base16 Encoding')
    print('6. Base16 Decoding')
    print('7. ASCII85 Encoding')
    print('8. ASCII85 Decoding')
    print('9. Base64 Encoding Files')
    print('10. Base64 Decoding Files\n')
    sel = input('Press 1/2/3/4/5/6/7/8/9/10 and press Enter, or press 0 and press Enter to go back to the main menu: ')
    clear()
    if sel == '1' or sel == '2' or sel == '9' or sel == '10':
        print('From Wikipedia: \n')
        print('"In programming, Base64 is a group of binary-to-text encoding schemes that represent binary data (more specifically, a sequence of 8-bit bytes) in an ASCII string format by translating the data into a radix-64 representation. The term Base64 originates from a specific MIME content transfer encoding. Each non-final Base64 digit represents exactly 6 bits of data. Three 8-bit bytes (i.e., a total of 24 bits) can therefore be represented by four 6-bit Base64 digits."\n')
        if sel == '1':
            base64_encode()
        elif sel == '2':
            base64_decode()
        elif sel == '9':
            base64_encode_file()
        elif sel == '10':
            base64_decode_file()
    elif sel == '3' or sel == '4':
        print('From Wikipedia: \n')
        print('"Base32 is the base-32 numeral system. It uses a set of 32 digits, each of which can be represented by 5 bits (25). One way to represent Base32 numbers in a human-readable way is by using a standard 32-character set, such as the twenty-six upper-case letters A–Z and the digits 2–7. However, many other variations are used in different contexts."\n')
        if sel == '3':
            base32_encode()
        elif sel == '4':
            base32_decode()
    elif sel == '5' or sel == '6':
        print('From Wikipedia: \n')
        print('"In mathematics and computing, the hexadecimal (also base 16 or hex) numeral system is a positional numeral system that represents numbers using a radix (base) of 16. Unlike the common way of representing numbers using 10 symbols, hexadecimal uses 16 distinct symbols, most often the symbols "0"–"9" to represent values 0 to 9, and "A"–"F" (or alternatively "a"–"f") to represent values 10 to 15. Hexadecimal is used in the transfer encoding Base16, in which each byte of the plaintext is broken into two 4-bit values and represented by two hexadecimal digits."\n')
        if sel == '5':
            base16_encode()
        elif sel == '6':
            base16_decode()
    elif sel == '7' or sel == '8':
        print('From Wikipedia: \n')
        print('"Ascii85, also called Base85, is a form of binary-to-text encoding developed by Paul E. Rutter for the btoa utility. By using five ASCII characters to represent four bytes of binary data (making the encoded size 1⁄4 larger than the original, assuming eight bits per ASCII character), it is more efficient than uuencode or Base64, which use four characters to represent three bytes of data (1⁄3 increase, assuming eight bits per ASCII character)."\n')
        if sel == '7':
            ascii85_encode()
        elif sel == '8':
            ascii85_decode()
    elif sel == '0':
        selection_menu_home()
    sel = input('Press s and enter to go back to the encoding/decoding selection menu and press 0 and enter to go back to the main menu: ')
    clear()
    if sel == 's':
        selection_encode_decode()
    elif sel == '0':
        selection_menu_home()

def selection_base_n():
    print('From Wikipedia: \n')
    print('"Positional notation (or place-value notation, or positional numeral system) denotes usually the extension to any base of the Hindu–Arabic numeral system (or decimal system). More generally, a positional system is a numeral system in which the contribution of a digit to the value of a number is the value of the digit multiplied by a factor determined by the position of the digit. In early numeral systems, such as Roman numerals, a digit has only one value: I means one, X means ten and C a hundred (however, the value may be negated if placed before another digit). In modern positional systems, such as the decimal system, the position of the digit means that its value must be multiplied by some value: in 555, the three identical symbols represent five hundreds, five tens, and five units, respectively, due to their different positions in the digit string."\n')
    print('In this program, these conversions have been implemented: \n')
    print('1. Converting a decimal integer to a base-n number,\n')
    print('2. Converting a base-n number to a decimal integer\n')
    sel = input('Press 1/2 and press Enter, or press 0 and press Enter to go back to the main menu: ')
    clear()
    if sel == '1':
        base_n_convert_int_base()
    elif sel == '2':
        base_n_convert_base_int()
    elif sel == '0':
        selection_menu_home()
    sel = input('Press s and enter to go back to the base-n conversion selection menu and press 0 and enter to go back to the main menu: ')
    clear()
    if sel == 's':
        selection_base_n()
    elif sel == '0':
        selection_menu_home()
    
def selection_hashing():
    print('From Wikipedia: \n')
    print('"A hash function is any function that can be used to map data of arbitrary size to fixed-size values. The values returned by a hash function are called hash values, hash codes, digests, or simply hashes. The values are usually used to index a fixed-size table called a hash table. Use of a hash function to index a hash table is called hashing or scatter storage addressing."\n')
    print('"Hash functions and their associated hash tables are used in data storage and retrieval applications to access data in a small and nearly constant time per retrieval, and require an amount of storage space only fractionally greater than the total space required for the data or records themselves. Hashing is a computationally and storage space efficient form of data access which avoids the non-linear access time of ordered and unordered lists and structured trees, and the often exponential storage requirements of direct access of state spaces of large or variable-length keys."\n')
    print('In this program, calculating hashes using MD5, SHA-1, SHA-256, SHA-512, SHA3-256 and SHA3-512 algorithms is supported.')
    sel = input('Press 1 and enter to hash a string, press 2 and enter to hash a file, or press 0 and enter to go back to the main menu: ')
    clear()
    if sel == '1':
        hash_string()
    elif sel == '2':
        hash_file()
    elif sel == '0':
        selection_menu_home()
    sel = input('Press s and enter to go back to the hash input-type selection menu and press 0 and enter to go back to the main menu: ')
    clear()
    if sel == 's':
        selection_hashing()
    elif sel == '0':
        selection_menu_home()


def bonus_freq_analysis():
    freq_analysis()
    sel = input('Press 0 and enter to go back to the main menu: ')
    clear()
    if sel == '0':
        selection_menu_home()

def bonus_morse_convert():
    print('From wikipedia: \n')
    print('"Morse code is a method used in telecommunication to encode text characters as standardized sequences of two different signal durations, called dots and dashes, or dits and dahs. Morse code is named after Samuel Morse, one of the inventors of the telegraph.\n"')
    print('"International Morse Code, also known as Continental Morse Code, encodes the 26 Latin letters A through Z, one non-Latin letter, the Arabic numerals, and a small set of punctuation and procedural signals (prosigns). There is no distinction between upper and lower case letters. Each Morse code symbol is formed by a sequence of dits and dahs. The dit duration is the basic unit of time measurement in Morse code transmission. The duration of a dah is three times the duration of a dit. Each dit or dah within an encoded character is followed by a period of signal absence, called a space, equal to the dit duration. The letters of a word are separated by a space of duration equal to three dits, and words are separated by a space equal to seven dits."\n')
    sel = input('Press 1 and enter to convert a string to morse code, press 2 and enter to convert morse code to plaintext, or press 0 and enter to go back to the main menu: ')
    if sel == '1':
        morse_encode()
    elif sel == '2':
        morse_decode()
    elif sel == '0':
        selection_menu_home()
    sel = input('Press s and enter to go back to the morse conversion selection menu and press 0 and enter to go back to the main menu: ')
    clear()
    if sel == 's':
        bonus_morse_convert()
    elif sel == '0':
        selection_menu_home()


if __name__=='__main__':
    main()
