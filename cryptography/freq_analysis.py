from matplotlib import pyplot as plt

def freq_analysis():
    print('From Wikipedia: ')
    print('"In cryptanalysis, frequency analysis (also known as counting letters) is the study of the frequency of letters or groups of letters in a ciphertext. The method is used as an aid to breaking classical ciphers."')
    print('"Frequency analysis is based on the fact that, in any given stretch of written language, certain letters and combinations of letters occur with varying frequencies. Moreover, there is a characteristic distribution of letters that is roughly the same for almost all samples of that language. For instance, given a section of English language, E, T, A and O are the most common, while Z, Q, X and J are rare. Likewise, TH, ER, ON, and AN are the most common pairs of letters (termed bigrams or digraphs), and SS, EE, TT, and FF are the most common repeats.[1] The nonsense phrase "ETAOIN SHRDLU" represents the 12 most frequent letters in typical English language text".\n')
    input_text = input('Enter a string to create a chart based on its letter frequency: ')
    input_text = input_text.upper()
    input_dict = dict()
    for char in input_text:
        if ord(char) >= 65 and ord(char) <= 90:
            if char not in input_dict:
                input_dict[char] = 1
            else:
                input_dict[char] += 1
    print('Now we will show the frequency distribution of the letters in the string.')
    plt.bar(input_dict.keys(), input_dict.values())
    plt.title('Frequency Distribution')
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.show()
