import csv
class Data:
    def __init__(self, path):
        self.path = path
        self.csv_matrix = []

    def load_csv(self):
        with open(self.path, mode= 'r', newline='', encoding='cp1252') as f:
            reader = csv.reader(f, delimiter=",")
            self.csv_matrix = list(reader)

