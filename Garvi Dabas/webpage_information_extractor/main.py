from WebPageFetcher import WebPageFetcher
from WebPageExtractor import WebPageExtractor
from WebPageData import WebPageData
from ReportSaver import ReportSaver

def main():

    url = input("Enter the URL of the webpage to scrape: ").strip()

    #Continue only if the user enters a URL.
    if not url:
        print("URL cannot be empty. You must enter a URL.")
        return
    
    # Create a fetcher for the given URL and fetch the webpage.
    fetcher = WebPageFetcher(url)

    print("\nFetching the webpage...")

    soup = fetcher.fetch_page()

    # Continue only if the webpage was fetched successfully.
    if soup:
        print("Fetched webpage successfully!\n")

        # Extract information such as the title, links, and headings.
        extractor = WebPageExtractor(soup)
        print("Extracting information...")

        page_title = extractor.get_page_title()

        if page_title:
            print(f"Title extracted successfully: {page_title}")
        else:
            print("No title tag found in the webpage.")

        all_links, unique_links = extractor.extract_links()

        if all_links:
            print("Links extracted successfully!")
        else:
            print("No links found in the webpage.")

        all_headings = extractor.extract_headings()

        if all_headings:
            print("Headings extracted successfully!")
        else:
            print("No headings found in the webpage.")

        print("Information extraction completed!\n")

        # Create the page data object using the extracted information.
        page_data = WebPageData(
                                url, 
                                page_title, 
                                all_links, 
                                unique_links, 
                                all_headings
                                )

        print("Generating report...")
        report = page_data.generate_report() 
        print("Report generated successfully!\n")

        # Save the generated report to a file.
        saver = ReportSaver()
        file_path = saver.save_report(url, report)

        #Checking if the report was saved successfully.
        if file_path:
            print(
                  f"The report is saved successfully!\n"
                  f"The report is saved at {file_path}\n\n"
                  )
        else:
            print("Error: Unable to save the report.\n\n")

        # Generate and display a summary of the extracted information.
        summary = page_data.generate_summary()
        print("The summary of the extracted information is displayed below.")
        print(summary)


# Run main() only when this file is executed directly.
if __name__ == "__main__":
    main()





