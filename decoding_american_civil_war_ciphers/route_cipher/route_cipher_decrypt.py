"""
Decrypt a path through a Union Route Cipher

Designed for whole-word transposition ciphers with variable rows & columns.
Assumes encryption began at either top or bottom of a column.
Key indicates the order ot read columns and the direction to traverse.
Negative column numbers mean start at the bottom and read up.
Positive column numbers mean start at top & read down.

Example below is for 4x4 matrix wit key -1 2 -3 4.
Note "0" is not allowed
Arrows show encryption route; for negtive key values read UP.

    1    2    3    4
 _____ _____ _____ ____
|  ^  |  |  |  ^  |  | | MESSAGE IS WRITTEN 
|__|__|__v__|__|__|__v_|
|  ^  |  |  |  ^  |  | | ACROSS EACH ROW
|__|__|__v__|__|__|__v_|
|  ^  |  |  |  ^  |  | | IN THIS MANNER
|__|__|__v__|__|__|__v_|
|  ^  |  |  |  ^  |  | | LAST ROW IS FILLED WITH DUMMY WORDS
|__|__|__v__|__|__|__v_|
START               END    

Required inputs - a text message, # of columns, # of rows, key string

Prints translated plaintext

16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19 cipher text originall+y

"""  

import sys 

#=================================================================================================
# USER INPUT:

# The string to be decrypted (type or paste between triple-quotes)
ciphertext = """PURE OF TWENTY THIS IF YOU I FRIGGIN THIS POPPYCOCK AND MESSAGE DOLLARS OWE CAN READ YOU REST IS COCAINE"""

# Number of columns i the transposition matrix:
COLS = 4 

# Number of rows in the transposition matrix:
ROWS = 5

# Key with spaces between numbers; Negative to read UP column (ex = -1 2 -3 4):
key = """ -1 2 -3 4 """

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE
#=================================================================================================

def main():
    """ Run program and print decrypted plaintext """
    print("\nCiphertext = {}".format(ciphertext))
    print("Trying {} columns".format(COLS))
    print("Trying {} rows".format(ROWS))
    print("Trying key = {}".format(key))

    #split elements into words, not letters
    cipherlist = list(ciphertext.split())
    validate_col_row(cipherlist)
    key_int = key_to_int(key)
    translation_matrix = build_matrix(key_int, cipherlist)
    plaintext = decrypt(translation_matrix)

    print("\nPlaintext = {}".format(plaintext))

def validate_col_row(cipherlist):
    """ Check tat input columns & rows are valid vs. message length. """
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher): #range excludes 1-column ciphers
        if len_cipher % i == 0:
            factors.append(i)
    print("\nLength of cipher = {}".format(len_cipher))
    print("Acceptable column/row values include: {}".format(factors))
    print()
    if ROWS * COLS != len_cipher:
        print("\nError - Input columns & rows not factors of length :" \
              "of cipher. Terminating program.", file=sys.stderr)
        sys.exit(1)

def key_to_int(key):
    """ Turn key into list of integers & check validity """
    key_int = [int(i) for i in key.split()]
    key_int_lo = min(key_int)
    key_int_hi = max(key_int)
    if len(key_int) != COLS or key_int_lo < -COLS or key_int_hi > COLS or 0 in key_int:
        print("\nError - Problem with key. Terminating.", file=sys.stderr)
        sys.exit(1)
    else:
        return key_int

def build_matrix(key_int, cipherlist):
    """ Turn every n items in a list into a new item in a list of lists. """
    translation_matrix = [None] * COLS
    start = 0 
    stop = ROWS
    for k in key_int:
        if k < 0: # read bottom-to-top of column
            col_items = cipherlist[start:stop]
        elif k > 0: # read top-to-bottom of column
            col_items = list((reversed(cipherlist[start:stop])))
        translation_matrix[abs(k) - 1] = col_items
        start += ROWS
        stop += ROWS
    return translation_matrix

def decrypt(translation_matrix):
    """ Loop through nested lists popping off last item to a string """
    plaintext = ''
    for i in range(ROWS):
        for matrix_col in translation_matrix:
            word = str(matrix_col.pop())
            plaintext += word + ' '
    return plaintext

if __name__ == '__main__':
    main()     