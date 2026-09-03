from file_analysis.file_reader import read_file
from file_analysis.general_stats import GeneralStats
from file_analysis.word_frequency import WordFrequency
from file_analysis.word_analyzer import WordAnalyzer
from file_analysis.report_generator import generate_report
from file_analysis.exceptions import InputValidationError, validate_input


def main():
    print("=" * 45)
    print("     FILE ANALYSIS AND REPORT GENERATOR")
    print("=" * 45)

    while True :

        try:
            file_name = input("\nEnter the valid path of the .txt file: (or press 1 to exit): ").strip()

            if file_name == "1":
                print("\nThank you for using File Analysis and Report Generator.")
                return

            validate_input(file_name, "File name cannot be empty.")

            text = read_file(file_name)

            if text is None:
                continue

            validate_input(text.strip(), "The file is empty.")

            stats = GeneralStats(text)

            word_frequency = WordFrequency(text)
            word_analyzer = WordAnalyzer(word_frequency.get_all_words_frequency())

            break

        except InputValidationError as e:
            print(f"Error : {e}")


    while True:
        print("\nChoose an option:")
        print("1. Count lines")
        print("2. Count words")
        print("3. Count characters")
        print("4. Display word frequency")
        print("5. Search for a word")
        print("6. Find frequency of a word")
        print("7. Find most frequent word(s)")
        print("8. Generate report")
        print("9. Display all statistics")
        print("10. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            print(f"\nNumber of lines: {stats.count_lines()}")

        elif choice == "2":
            print(f"\nNumber of words: {stats.count_words()}")

        elif choice == "3":
            print(f"\nNumber of characters: {stats.count_characters()}")

        elif choice == "4":
            word_frequency.display_all_words_frequency()

        elif choice == "5":

            while True :

                try:
                    word = input("\nEnter a valid word to search"
                                 "(or press 1 to go back to main menu): ").strip()

                    if word == "1":
                        break

                    validate_input(word, "word cannot be empty.")

                    if word_analyzer.search_word(word):
                        print(f"'{word}' is present in the file.")
                    else:
                        print(f"'{word}' is not present in the file.")

                    break

                except InputValidationError as e:
                    print(f"Error : {e}")

        elif choice == "6":

            while True :

                try: 
                    word = input("\nEnter the word"
                                 "(or press 1 to go back to main menu): ").strip()

                    if word == "1":
                        break;

                    validate_input(word, "Word cannot be empty")

                    frequency = word_analyzer.get_word_frequency(word)
                    print(f"'{word}' appears {frequency} time(s).")

                    break

                except InputValidationError as e:
                    print(f"Error : {e}")

        elif choice == "7":

            most_frequent_words = word_analyzer.get_most_frequent_words()

            print("\nMost frequently used word(s):")
            for word in most_frequent_words:
                print(f"{word} : {word_frequency.get_all_words_frequency()[word]}")

        elif choice == "8":

            while True :

                try:
                    report_name = input(
                        "\nEnter report file name (for example, report.txt)"
                         "(or press 1 to go back to main menu): "
                    ).strip()

                    if report_name == "1":
                        break;
                    
                    validate_input(report_name, "Report name cannot be empty.")

                    generate_report(
                        report_name,
                        stats.count_lines(),
                        stats.count_words(),
                        stats.count_characters(),
                        word_frequency.frequency,
                        word_analyzer.get_most_frequent_words(),
                    )

                    break

                except InputValidationError as e:
                    print(f"Error : {e}")

        elif choice == "9":
            stats.display_general_stats()
            word_frequency.display_all_words_frequency()

        elif choice == "10":
            print("\nThank you for using File Analysis and Report Generator.")
            break

        else:
            print("Error: Invalid choice. Please select an option from 1 to 10.")


if __name__ == "__main__":
    main()