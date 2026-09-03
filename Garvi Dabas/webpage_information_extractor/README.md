WEBPAGE INFROMATION EXTRACTOR

1. Project Description:

 This project "Webpage Informatin Extractor" is a Python-based application that fetches a webpage and extracts useful information from it.

 The project takes a URL as uer input, fetches the URL, then extracts the information and generates report and summary of the information extracted. The summary is displayed in the terminal and the report generated is saved in the folder saved_reports.

 The project is designed using multiple classes, where each class has a specific responsibility.



2. Implemented features:
 
 - Fetches a webpage using a user-provided URL.
 - Handles common request and connection errors.
 - Extracts the webpage title.
 - Extracts all links from the webpage.
 - Identifies unique links.
 - Extracts h1, h2 and h3 headings.
 - Generates a detailed report containing the extracted information.
 - Generates a summary showing the number of headings and links.
 - Saves the generated report as a text file.
 - Creates the report directory automatically if it does not already exist.
 - Uses a timestamp in the filename to help make report filenames unique.
 - Handles common file and directory errors.



3. Instructions to run the application:

 - Make sure Python is installed on your system.
 - Install the required packages: pip install requests beautifulsoup4
 - Open a terminal in the project directory.
 - Run the application:
 - python main.py
 - Enter a valid webpage URL when prompted:
    - Enter the URL of the webpage to scrape: https://www.nasa.gov/     
 - The application will:
    - Fetch the webpage.
    - Extract the webpage title, links, and headings.
    - Generate a report.
    - Save the report inside the saved_reports directory.
    - Display a summary of the extracted information in the terminal.
 

 
4. Required packages:
 
 The following Python packages are required:
 - requests – Used to send HTTP requests and fetch webpage content.
 - beautifulsoup4 – Used to parse HTML and extract webpage information.

 The following modules are part of the Python standard library and do not need to be installed separately:
 - pathlib
 - urllib.parse
 - datetime



5. Known limitations:
 
  The following are the known limitations of the package:
  - Some websites use JavaScript to load their content, so the application may not be able to extract all the information from those websites.
  - The application cannot extract information from a webpage if the website does not allow access to its content.
  - The application extracts information directly available in the HTML response.
  - Some websites may block automated requests.
  