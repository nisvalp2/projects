# NATO Phonetic Alphabet Converter

This script converts a user-provided word into its NATO phonetic alphabet equivalent.

## How It Works

1. The script reads a CSV file (`nato_phonetic_alphabet.csv`) containing the NATO phonetic alphabet, with each row representing a letter and its corresponding phonetic code.
2. It creates a dictionary mapping each letter to its phonetic code.
3. The user is prompted to enter a word.
4. The script converts the word into a list of phonetic codes using the dictionary.
5. The phonetic code list is displayed.

## Requirements

- Python 3.x
- Pandas library

## Setup

1. Ensure you have Python installed on your system.
2. Install the Pandas library if not already installed:
   ```bash
   pip install pandas
