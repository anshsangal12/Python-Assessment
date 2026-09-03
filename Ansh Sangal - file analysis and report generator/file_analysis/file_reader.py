def read_file(file_name):
    if not file_name.lower().endswith(".txt"):
        print("Error: Only .txt files are supported.")
        return None

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        print("Error: File not found.")
        return None

    except UnicodeDecodeError:
        print("Error: File does not contain valid UTF-8 text.")
        return None