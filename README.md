# Flashcard Quiz

A command-line study tool written in Python. Load a deck of flashcards from a JSON file and get quizzed on it. Cards you miss come back until you get them right, and you get a score at the end.

## Features

- Shuffled quizzes from any JSON deck
- Missed cards return to the queue until answered correctly
- Answers ignore capitalization and extra spaces
- Type `quit` any time to stop
- Easy to make your own decks

## Usage

Requires Python 3.8 or newer. No external libraries needed.

```
python flashcards.py decks/python_basics.json
```

Example session:

```
Loaded 9 cards. Type 'quit' to stop.

Q: What keyword defines a function in Python?
> def
Correct!

Q: What is 7 // 2?
> 4
Not quite. The answer is: 3
```

## Making your own deck

A deck is a JSON file containing a list of cards. Each card has a `question` and an `answer`:

```json
[
  {"question": "Capital of France?", "answer": "Paris"},
  {"question": "Largest planet?", "answer": "Jupiter"}
]
```

Save it in the `decks` folder and run it the same way.

## Running the tests

```
python -m unittest
```

## How it works

- `load_deck` reads and validates a JSON deck.
- `run_quiz` keeps a queue of cards, pops one at a time, and puts missed cards back at the end. It takes `ask` and `show` parameters so tests can replace `input()` and `print()`.
- `test_flashcards.py` uses `unittest` to cover perfect runs, missed cards, and quitting early.

## Ideas for next steps

- Save your best scores for each deck
- Add a `--count` option to quiz on only some of the cards
- Show which cards you missed most at the end
