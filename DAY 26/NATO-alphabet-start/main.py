import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

dict = {row.letter: row.code for (index, row) in df.iterrows()}

user_input = input("Enter a word: ").upper()
codes_list = [dict[letter] for letter in user_input]
print(codes_list)
