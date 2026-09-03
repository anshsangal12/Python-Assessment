class WordAnalyzer:
    def __init__(self, word_frequency):
        self.word_frequency = word_frequency

    def search_word(self, word):
        return word.lower() in self.word_frequency

    def get_word_frequency(self, word):
        return self.word_frequency.get(word.lower(), 0)

    def get_most_frequent_words(self):
        if not self.word_frequency:
            return []

        highest_frequency = max(self.word_frequency.values())

        return [
            word
            for word, frequency in self.word_frequency.items()
            if frequency == highest_frequency
        ]