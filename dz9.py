"""Reading the file and writing to the new file."""
# Declaration  the new function
def find_english_alphabet_positions(input_file, output_file):
    # Opening the file for reading
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    english_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    found_letters = {}

    # Finding all characters from the English
    # alphabet and their positions
    for pos, char in enumerate(content):
        if char in english_alphabet:
            if char not in found_letters:
                found_letters[char] = pos

    # Recording the results in the "output.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        for letter, pos in found_letters.items():
            f.write(f'{letter} -> pos{pos}\n')

# Runing the function with files
find_english_alphabet_positions('input.txt', 'output.txt')
