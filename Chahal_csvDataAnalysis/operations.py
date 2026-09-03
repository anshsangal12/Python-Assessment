from collections import defaultdict

from validator import validate_data


class Operations:
    def __init__(self, csv_matrix, start, end):
        self.csv_matrix = csv_matrix
        self.start = start
        self.end = end

    def group_records(self, col_index):
        groups = {}
        for row in self.csv_matrix[self.start:self.end]:
            key = row[col_index].strip()
            if key not in groups:
                groups[key] = []
            groups[key].append(row)
        return groups


class Numeric_Operations(Operations):
    def get_valid_values(self, column_index):
        valid_values = []
        invalid_values_count = 0
        for row in self.csv_matrix[self.start: self.end]:
            val = row[column_index]
            if validate_data(val, True):  #true because it is in the numeric class
                valid_values.append(float(val))
            else:
                invalid_values_count += 1
        return valid_values, invalid_values_count


    def calculate_total(self, valid_values):
        return sum(valid_values)

    def calculate_average(self, valid_values):
        return sum(valid_values) / len(valid_values)

    def get_highest_score(self, valid_values):
        return max(valid_values)

    def get_lowest_score(self, valid_values):
        return min(valid_values)

    def get_median(self, valid_values):
        copy_valid_values = valid_values.copy()
        copy_valid_values.sort()
        # copy_valid_values = sorted(valid_values)
        total_values = len(copy_valid_values)
        if (total_values & 1) == 1:
            return copy_valid_values[(total_values - 1) // 2]
        else:
            return (copy_valid_values[(total_values - 1) // 2] + copy_valid_values[total_values // 2]) / 2


class String_Operations(Operations):
    def get_valid_values(self, column_index):
        valid_values = []
        invalid_values_count = 0
        for row in self.csv_matrix[self.start: self.end]:
            val = row[column_index].strip()
            if validate_data(val, False):
                valid_values.append(val)
            else:
                invalid_values_count += 1
        return valid_values, invalid_values_count

    def get_highest_occurring(self, valid_values):

        frequency_map = defaultdict(int)

        for element in valid_values:
            frequency_map[element] += 1

        highest_frequent_key = max(frequency_map, key=frequency_map.__getitem__)
        return highest_frequent_key, frequency_map[highest_frequent_key]

    def get_lowest_occurring(self, valid_values):
        frequency_map = defaultdict(int)

        for element in valid_values:
            frequency_map[element] += 1

        lowest_frequent_key = min(frequency_map, key=frequency_map.__getitem__)
        return lowest_frequent_key, frequency_map[lowest_frequent_key]

