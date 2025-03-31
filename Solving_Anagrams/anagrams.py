import load_dictionary

word_list = load_dictionary.load("project_dict.txt")

anagram_list = []

# Input a single WORD or NAME to find its anagram(s).
print("Enter a Name! A word will work as well.\n")
name = input("Input Here: ")
print("Input name = {}".format(name))
name = name.lower()
print("Using name = {}".format(name))

#sort name and find anagrams
name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

#print out list of anagrams
print()
if len(anagram_list) == 0:
    print("This dictionary couldn't handle the power of {}!(No anagrams found)".format(name))
else:
    print("Anagrams =", *anagram_list, sep='\n')