def generate_report(
    file_name,
    lines,
    words,
    characters,
    word_frequency,
    most_frequent_words,
):

    with open(f"{file_name}.txt", "w", encoding="utf-8") as file:
        file.write("FILE ANALYSIS REPORT\n")
        file.write("=" * 45 + "\n\n")

        file.write(f"Number of lines      : {lines}\n")
        file.write(f"Number of words      : {words}\n")
        file.write(f"Number of characters : {characters}\n\n")

        file.write("MOST FREQUENT WORD(S)\n")
        file.write("-" * 45 + "\n")

        for word in most_frequent_words:
            file.write(f"{word} : {word_frequency[word]}\n")

        file.write("\nWORD FREQUENCY\n")
        file.write("-" * 45 + "\n")

        for word, frequency in word_frequency.items():
            file.write(f"{word:<25} : {frequency}\n")

    print(f"\nReport generated successfully: {file_name}")