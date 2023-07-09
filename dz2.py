""" Counting and replacing vowels in text. """

poem_text = """I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze. 

Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance."""

#Counting the occurrences of vowels in the text

vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
for letter in poem_text.lower():
    if letter in vowels:
        vowels[letter] += 1

# Outputting the count of each vowel as a table

print('-----------------')
print('| vowel | count |')
print('-----------------')
for vowel in vowels:
    print(f'|   {vowel}   |  {vowels[vowel]:2d}   |')
print('-----------------')

# Replacing the vowels with accentuated characters
vowel_replacements = {'A': 'À', 'a': 'à', 'E': 'É', 'e': 'é', 'I': 'Í',
                     'i': 'í', 'O': 'Ó', 'o': 'ó', 'U': 'Ú', 'u': 'ú'}
poem_text_replaced = ''
for letter in poem_text:
    if letter in vowel_replacements:
        poem_text_replaced += vowel_replacements[letter]
    else:
        poem_text_replaced += letter

print(poem_text_replaced)
