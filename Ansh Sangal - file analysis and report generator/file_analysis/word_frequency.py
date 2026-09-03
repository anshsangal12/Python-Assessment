import string

class WordFrequency:
    def __init__(self, text):
        self.frequency = self.calculate_frequency(text)

    def calculate_frequency(self, text):
        words_frequency = {}

        for word in self.get_clean_words(text):
            if word in words_frequency:
                words_frequency[word] += 1
            else:
                words_frequency[word] = 1

        return words_frequency

    def get_clean_words(self, text):
        text = text.lower()

        for punctuation in string.punctuation:
            text = text.replace(punctuation, "")

        return text.split()

    def get_all_words_frequency(self):
        return self.frequency

    def display_all_words_frequency(self):
        print("\nWord Frequency:")
        print("-" * 15)

        for word, frequency in self.frequency.items():
            print(f"{word : <8} : {frequency}")