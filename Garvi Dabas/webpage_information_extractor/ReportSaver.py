from pathlib import Path
from urllib.parse import urlparse
from datetime import datetime

class ReportSaver:

    def __init__(self, save_directory="saved_reports"):
        # Store the directory where generated reports will be saved.
        self.save_directory = Path(save_directory)

    # Save the generated report using the webpage domain and current timestamp.
    def save_report(self, url, report):
        try:

            #Create reports directory if it does not already exists.
            self.save_directory.mkdir(exist_ok=True)

            #Generate a timestamp to make each report filename unique.
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            #Extract the domain from the webpage URL.
            parsed = urlparse(url)
            domain = parsed.netloc
            domain = domain.replace("www.", "")

            #Create the filename and file path then writing the report to the file.
            filename = domain + "_" + timestamp + ".txt"
            filepath = self.save_directory/filename
            filepath.write_text(report, encoding="utf-8")

            return filepath

        #Handle errors that occur while creating or writing the file.
        except OSError:
            print("Could not save the report.")
            return None
        
