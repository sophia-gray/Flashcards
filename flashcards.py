"""Flashcard Quiz

A command-line study tool. Load a deck of question/answer cards from a JSON
file and get quizzed. Cards you miss go back into the queue until you answer
them correctly, and you get a score at the end.

Usage:
    python flashcards.py decks/python_basics.json
"""

import argparse
import json
import random


def load_deck(path):
    """Read a deck from a JSON file and check that every card is valid."""
    with open(path) as f:
        cards = json.load(f)
    for card in cards:
        if "question" not in card or "answer" not in card:
            raise ValueError("Every card needs a 'question' and an 'answer'.")
    return cards


def check_answer(guess, answer):
    """Compare a guess to the answer, ignoring case and extra spaces."""
    return guess.strip().lower() == answer.strip().lower()


def run_quiz(cards, ask=input, show=print, shuffle=True):
    """Quiz the user until every card is answered correctly.

    Missed cards go to the back of the queue. Returns a tuple of
    (cards right on the first try, total cards, whether the quiz was finished).
    The ask and show parameters let tests replace input() and print().
    """
    queue = list(cards)
    if shuffle:
        random.shuffle(queue)

    total = len(queue)
    missed = set()
    first_try_correct = 0

    while queue:
        card = queue.pop(0)
        try:
            guess = ask(f"Q: {card['question']}\n> ")
        except (EOFError, KeyboardInterrupt):
            print()  # Ctrl+C / Ctrl+D counts as quitting
            return first_try_correct, total, False

        if guess.strip().lower() in ("quit", "q"):
            return first_try_correct, total, False

        if check_answer(guess, card["answer"]):
            show("Correct!\n")
            if card["question"] not in missed:
                first_try_correct += 1
        else:
            show(f"Not quite. The answer is: {card['answer']}\n")
            missed.add(card["question"])
            queue.append(card)

    return first_try_correct, total, True


def main():
    parser = argparse.ArgumentParser(description="Quiz yourself with flashcards.")
    parser.add_argument("deck", help="path to a JSON deck file")
    args = parser.parse_args()

    cards = load_deck(args.deck)
    print(f"Loaded {len(cards)} cards. Type 'quit' to stop.\n")

    score, total, finished = run_quiz(cards)

    if finished:
        print(f"Done! You got {score}/{total} right on the first try.")
    else:
        print(f"Stopped early. You got {score} right on the first try.")


if __name__ == "__main__":
    main()
