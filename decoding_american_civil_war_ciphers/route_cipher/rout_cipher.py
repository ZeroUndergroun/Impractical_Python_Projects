ciphertext = "PURE OF TWENTY THIS IF YOU I FRIGGIN THIS POPPYCOCK AND MESSAGE DOLLARS OWE CAN READ YOU REST IS COCAINE"

#split elements into words, not letters
cipherlist = list(ciphertext.split())

#initiailize our variables
COLS = 4
ROWS = 5
key = '-1 2 -3 4' # a neg number means read up columns vs. DOWN
translation_matrix = [None] * COLS
plaintext = ''
start = 0
stop = ROWS

#turn key into list of integers
key_int = [int(i) for i in key.split()]

#turn columns into items in list of lists
for k in key_int:
    if k < 0:  # reading bottom-to-top of column
        col_items = cipherlist[start:stop]
    elif k > 0:
        col_items = list((reversed(cipherlist[start:stop])))
    translation_matrix[abs(k) - 1] = col_items
    start += ROWS
    stop += ROWS 

print("\nciphertext = {}".format(ciphertext))
print("\ntranslation matrix = ", *translation_matrix, sep="\n")
print("\nkey length = {}".format(len(key_int)))

# loop through nested lists popping off last item to new list:
for i in range(ROWS):
    for col_items in translation_matrix:
        word = str(col_items.pop())
        plaintext += word + ' '

print("\nplaintext = {}".format(plaintext))