def base_n_convert_int_base():
    number = input('Enter a decimal integer to be converted to a number of base n: ')
    number = int(eval(number))
    base = int(input('Enter the base of the desired number: '))
    base_20_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    number_conv = ''
    if number == 0:
        number_conv = '0'
    elif base <= 36:
        while number != 0:
            conv_dig = int(number % base)
            conv_dig = base_20_lst[conv_dig]
            number_conv += conv_dig
            number //= base
        number_conv = number_conv[::-1]
    else:
        number_conv = []
        while number != 0:
            conv_dig = int(number % base)
            number_conv.append(str(conv_dig))
            number //= base
        number_conv = number_conv[::-1]
        number_conv = ', '.join(number_conv)
    print('The converted number is: ' + number_conv)

def base_n_convert_base_int():
    number = input('Enter a base-n number to be converted to a decimal integer: ')
    base_given = int(input('Enter the base of the entered number: '))
    number_conv = ''
    if number == 0:
        number_conv = '0'
    elif base_given <= 36:
       number_conv = str(int(number, base_given))
    else:
        number_conv = 0
        number = number.split(', ')
        number.reverse()
        for i in range(len(number)):
            number_conv += int(number[i]) * base_given ** i
        number_conv = str(number_conv)
    print('The converted number is: ' + number_conv)
