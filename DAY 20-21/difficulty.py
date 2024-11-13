class Difficulty:
    def __init__(self):
        self.difficulty = ""

    def set_difficulty(self, screen):
        self.difficulty = ""
        while (
            self.difficulty != "easy"
            and self.difficulty != "hard"
            and self.difficulty != "normal"
        ):
            self.difficulty = screen.textinput(
                title="Difficulty", prompt="Choose difficulty: \n(Easy/Normal/Hard)"
            ).lower()
        if self.difficulty.lower() == "easy":
            self.difficulty_num = 0.2
        elif self.difficulty.lower() == "normal":
            self.difficulty_num = 0.1
        elif self.difficulty.lower() == "hard":
            self.difficulty_num = 0.05
