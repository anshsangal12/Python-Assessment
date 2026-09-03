class WebPageData:

    def __init__(self, url, title, all_links, unique_links, all_headings):
        # Store the webpage information extracted by WebPageExtractor.
        self.url = url
        self.title = title
        self.all_links = all_links
        self.unique_links = unique_links
        self.all_headings = all_headings


    # Generate a complete report containing the extracted webpage information.
    def generate_report(self):

        # Add the report header.
        report = (
            "=" * 50 + "\n"+
            "WEBPAGE EXTRACTED INFORMATION REPORT\n"+
            "=" * 50 + "\n\n"
        )

        # Add the webpage URL to the report.
        report += f"URL:\n{self.url}\n\n"

        # Add the webpage title or a message if no title was found.
        if self.title:
            report += f"TITLE:\n{self.title}\n\n"
        else:
            report += f"TITLE:\nNo title found.\n\n"

        # Add the extracted headings to the report.
        report += "-" * 50 + "\n"
        report += "HEADINGS\n"
        report += "-" * 50 + "\n"

        if self.all_headings:
            for index, heading in enumerate(self.all_headings):
                report += f"{index+1}. {heading}\n"
        else:
            report += "No headings found.\n"
        report += "\n"

        # Add the unique links to the report.
        report += "-" * 50 + "\n"
        report += "LINKS\n"
        report += "-" * 50 + "\n"

        if self.unique_links:
            for index, link in enumerate(self.unique_links):
                report += f"{index+1}. {link}\n"
        else:
            report += "No links found.\n"    
        report += "\n"

        # Add a summary of the extracted information.
        report += self.generate_summary()
        report += "\n"

        # Add the report completion message.
        report += "=" * 50 + "\n"
        report += "REPORT GENERATED SUCCESSFULLY\n"
        report += "=" * 50 + "\n"  

        return report


    # Generate a summary containing counts of the extracted information.
    def generate_summary(self):

        summary = ""

        # Add the summary header.
        summary += "-" * 50 + "\n"
        summary += "SUMMARY\n"
        summary += "-" * 50 + "\n"

        # Add the webpage URL.
        summary += f"\nURL: {self.url}\n"

        # Add the webpage title or a message if no title was found.
        if self.title:
            summary += f"TITLE: {self.title}\n"
        else:
            summary += "TITLE: No title found.\n"

        # Add the total number of headings and links.
        summary += f"Total Headings: {len(self.all_headings)}\n"
        summary += f"Total Links: {len(self.all_links)}\n"

        # Add the unique link count only when duplicate links exist.
        if len(self.all_links) != len(self.unique_links):
            summary += f"Total Unique Links: {len(self.unique_links)}\n"

        return summary





        