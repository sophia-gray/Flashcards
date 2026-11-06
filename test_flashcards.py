import unittest

from flashcards import check_answer, run_quiz

CARDS = [
    {"question": "2 + 2?", "answer": "4"},
    {"question": "Capital of Canada?", "answer": "Ottawa"},
]


def fake_input(replies):
    """Return an ask() function that gives back the replies one at a time."""
    replies = iter(replies)
    return lambda prompt: next(replies)


class FlashcardTests(unittest.TestCase):
    def test_check_answer_ignores_case_and_spaces(self):
        self.assertTrue(check_answer("  OTTAWA ", "Ottawa"))
        self.assertFalse(check_answer("Toronto", "Ottawa"))

    def test_perfect_run(self):
        score, total, finished = run_quiz(
            CARDS, ask=fake_input(["4", "Ottawa"]), show=lambda s: None, shuffle=False
        )
        self.assertEqual((score, total, finished), (2, 2, True))

    def test_missed_card_comes_back(self):
        # Wrong answer first, then correct when the card returns.
        score, total, finished = run_quiz(
            CARDS, ask=fake_input(["5", "Ottawa", "4"]), show=lambda s: None, shuffle=False
        )
        self.assertEqual((score, total, finished), (1, 2, True))

    def test_quit_stops_early(self):
        score, total, finished = run_quiz(
            CARDS, ask=fake_input(["4", "quit"]), show=lambda s: None, shuffle=False
        )
        self.assertEqual((score, total, finished), (1, 2, False))

    def test_ctrl_d_stops_early(self):
        def raise_eof(prompt):
            raise EOFError

        score, total, finished = run_quiz(
            CARDS, ask=raise_eof, show=lambda s: None, shuffle=False
        )
        self.assertEqual((score, total, finished), (0, 2, False))


if __name__ == "__main__":
    unittest.main()
