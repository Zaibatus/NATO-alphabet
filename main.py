import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
game_off = False
while not game_off:
    word = input("enter a word: ").upper()
    if word == "END":
        game_off = True
    else:
        try:
            output_list = [nato_dict[letter] for letter in word]
        except KeyError:
            print("Sorry, only letters in the alphabet please.")
        else:
            print(output_list)
