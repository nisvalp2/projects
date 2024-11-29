# U.S. States Game

This is a Python-based game where the user tries to name all 50 U.S. states by typing their names. Correct guesses are displayed on a map, and at the end of the game, any missed states are saved to a CSV file for further review.

## How to Play

1. Run the script in a Python environment that supports `turtle` and `pandas`.
2. A map of the United States will appear.
3. A prompt will ask you to enter the name of a state.
4. If the state is correct, it will be displayed on the map.
5. The game ends when:
   - You guess all 50 states correctly.
   - You type "Exit" to stop the game.

## Features

- **State Tracking**: Tracks which states you have guessed correctly.
- **Missed States**: Saves a list of states you missed to a CSV file (`missed_states_to_learn.csv`).
- **Interactive Map**: Displays your correct guesses directly on the U.S. map.

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- `turtle` (built into Python)
- `pandas` (install via `pip install pandas`)

## Setup

1. Clone or download this repository.
2. Ensure you have the file `50_states.csv` in the same directory. This file should contain:
   - A column `state` with state names.
   - Columns `x` and `y` with coordinates for placing the state names on the map.
3. Place the `blank_states_img.gif` file in the same directory. This is the map image used in the game.

## How to Run

1. Open a terminal or Python IDE in the project directory.
2. Run the script:
   ```bash
   python your_script_name.py
