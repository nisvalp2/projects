import pandas

alphabet_data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')


alphabet_data = {row["letter"]:row["code"] for (index, row) in alphabet_data_frame.iterrows()}
print(alphabet_data)
word = (input('Enter a word: ').upper())

word_list = [alphabet_data[x] for x in word]
print(word_list)
