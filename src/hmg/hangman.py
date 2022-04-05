class Hangman:
    def __init__(self, secret_word, char_board="-"):
        self.secret_word = list(secret_word)
        self.secret_word_letters = set(self.secret_word)
        self.letters_used = set()
        self.char_board = char_board
        self.board = [self.char_board for _ in range(len(self.secret_word))]

    @property
    def is_completed(self):
        return self.board.count(self.char_board) == 0

    @staticmethod
    def letter_is_valid(letter: str) -> str:
        valid_letter = True
        if letter.isdigit() or not letter:
            valid_letter = False
        return valid_letter

    def char_is_used(self, char: str) -> bool:
        is_used = char in self.letters_used
        self.letters_used.add(char)
        return is_used

    def letter_in_the_word(self, entered_letter: str) -> bool:
        if entered_letter in self.secret_word_letters:
            self.secret_word_letters.remove(entered_letter)
            return True
        return False

    def update_dashboard(self, entered_letter: str) -> None:
        for _ in range(self.secret_word.count(entered_letter)):
            index = self.secret_word.index(entered_letter)
            self.secret_word.pop(index)
            self.secret_word.insert(index, self.char_board)
            self.board.pop(index)
            self.board.insert(index, entered_letter)
