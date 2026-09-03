from operations import Operations, Numeric_Operations, String_Operations

class Report:
    def __init__(self, path):
        self.report_content = ""


    def generate_report(self,ops, column_index, column_name, is_numeric):
        lines = []
        lines.append("=" * 50)
        lines.append(f"Column: {column_name}")
        lines.append( f"Row range: {ops.start} to {ops.end - 1}")
        lines.append("-" * 50)
        if is_numeric:
            valid_values, invalid_values_count = ops.get_valid_values(column_index)
            lines.append(f"valid entries: {len(valid_values)}")
            lines.append(f"invalid/missing : {invalid_values_count}")
            lines.append("-" * 50)
            if len(valid_values) == 0:
                lines.append("No valid Numeric values found")
            else:
                total = ops.calculate_total(valid_values)
                average = ops.calculate_average(valid_values)
                highest = ops.get_highest_score(valid_values)
                lowest = ops.get_lowest_score(valid_values)
                median = ops.get_median(valid_values)
                lines.append(f"Total: {total}")
                lines.append(f"Average: {average}")
                lines.append(f"Highest: {highest}")
                lines.append(f"Lowest: {lowest}")
                lines.append((f"Median: {median}"))
        else:
            valid_values, invalid_values_count = ops.get_valid_values(column_index)
            lines.append(f"valid entries: {len(valid_values)}")
            lines.append(f"invalid/missing : {invalid_values_count}")
            lines.append("-" * 50)
            if len(valid_values) == 0:
                lines.append("No valid String values found")
            else:
                highest_frequency_element, highest_frequency = ops.get_highest_occurring(valid_values)
                lowest_frequency_element, lowest_frequency = ops.get_lowest_occurring(valid_values)
                total_unique_values = len(set(valid_values))
                lines.append(f"Most occurring: {highest_frequency_element} -> {highest_frequency} times")
                lines.append(f"Least occurring: {lowest_frequency_element} -> {lowest_frequency} times")
                lines.append(f"Unique Values: {total_unique_values}")
        lines.append("=" * 50)

        section = "\n".join(lines) + "\n"
        self.report_content += section + "\n"
        return section

    def add_groups_to_report(self, groups, column_name):
        lines = []
        lines.append(f"Grouped By '{column_name}'")
        lines.append("-" * 50)
        # for key, rows in groups.items():
        for key, rows in sorted(groups.items(), key=lambda x: len(x[1]), reverse=True):
            if key.strip() != "":
                lines.append(f" {key} -> {len(rows)} record(s)")
        lines.append("=" * 50)
        section = "\n".join(lines) + "\n"
        self.report_content += section + "\n"
        return section

    def export_report(self, output_path):
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(self.report_content)
