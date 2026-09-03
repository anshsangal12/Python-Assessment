class GeneralStats:
    def __init__(self, text):
        self.text = text

    def count_lines(self):
        return len(self.text.splitlines())

    def count_words(self):
        return len(self.text.split())

    def count_characters(self):
        return len(self.text.replace("\n", ""))

    def display_general_stats(self):
        print("\n--- File Statistics ---")
        print(f"Number of lines      : {self.count_lines()}")
        print(f"Number of words      : {self.count_words()}")
        print(f"Number of characters : {self.count_characters()}")