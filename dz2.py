"""Counting and replacing vowels in text."""
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

vowels = ['A', 'E', 'I', 'O', 'U']

# Count the occurrences of each vowel

counts = {}
for vowel in vowels:
    counts[vowel] = poem_text.count(vowel) +\
                    poem_text.count(vowel.lower())

# Outputting the count of each vowel as a table
# Print the table header

summary = 'table printing completed'
print('Vowel count table:')
sep_num = 25
print('_' * sep_num)
print(f"| {'vowel':^9} | {'count':^9} |")
print('-' * sep_num)

# Print the vowel counts

for vowel, count in counts.items():
    print(f'|{vowel:^11}| {count:^9} |')

# Print the table footer
print('-' * sep_num)

# modify text where each vowel replaced

vowel_replacements = {'A': 'À', 'a': 'à',
                      'E': 'É', 'e': 'é',
                      'I': 'Í', 'i': 'í',
                      'O': 'Ó', 'o': 'ó',
                      'U': 'Ú', 'u': 'ú'}

modified_text = poem_text
for vowel, replacement in vowel_replacements.items():
    modified_text = modified_text.replace(vowel, replacement)
print('Modify text where each vowel replaced :')
print(modified_text)
