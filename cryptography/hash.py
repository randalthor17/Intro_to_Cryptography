from file_folder_chooser import file_chooser
from hashlib import *
ENCODING = 'utf-8'
BLOCK_SIZE = 65536

def hash_string():
    string = bytes(input('Enter a string to hash: '), ENCODING)
    print('\n')
    md5_hash = md5(string)
    sha1_hash = sha1(string)
    sha256_hash = sha256(string)
    sha512_hash = sha512(string)
    sha3_256_hash = sha3_256(string)
    sha3_512_hash = sha3_512(string)
    print('MD5: ' + md5_hash.hexdigest().upper())
    print('SHA-1: ' + sha1_hash.hexdigest().upper())
    print('SHA-256: ' + sha256_hash.hexdigest().upper())
    print('SHA-512: ' + sha512_hash.hexdigest().upper())
    print('SHA3-256: ' + sha3_256_hash.hexdigest().upper())
    print('SHA3-512: ' + sha3_512_hash.hexdigest().upper())

def hash_file():
    print('Choose the input file to be hashed.')
    input_file_location = file_chooser()
    md5_hash = md5()
    sha1_hash = sha1()
    sha256_hash = sha256()
    sha512_hash = sha512()
    sha3_256_hash = sha3_256()
    sha3_512_hash = sha3_512()
    with open(input_file_location, 'rb') as input_file:
        input_block = input_file.read(BLOCK_SIZE)
        while len(input_block) > 0:
            md5_hash.update(input_block)
            sha1_hash.update(input_block)
            sha256_hash.update(input_block)
            sha512_hash.update(input_block)
            sha3_256_hash.update(input_block)
            sha3_512_hash.update(input_block)
            input_block = input_file.read(BLOCK_SIZE)
    print('MD5: ' + md5_hash.hexdigest().upper())
    print('SHA-1: ' + sha1_hash.hexdigest().upper())
    print('SHA-256: ' + sha256_hash.hexdigest().upper())
    print('SHA-512: ' + sha512_hash.hexdigest().upper())
    print('SHA3-256: ' + sha3_256_hash.hexdigest().upper())
    print('SHA3-512: ' + sha3_512_hash.hexdigest().upper())

hash_file()