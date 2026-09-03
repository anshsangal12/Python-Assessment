class WebPageExtractor:

    def __init__(self, soup):
        #Storing the parsed webpage for extracting information.
        self.soup = soup


    #Extracting and returning the webpage title.
    def get_page_title(self):
        title = self.soup.title

        if title:
            return title.get_text(strip=True)
        
        return None

    #Extracting and returning the links.
    def extract_links(self):
        links = self.soup.find_all("a")

        all_links = []
        unique_links = set()
        
        for link in links:
            href = link.get("href")
            if href:
                all_links.append(href)
                unique_links.add(href)

        return all_links, unique_links

        
    #Extracting and returning the headings.
    def extract_headings(self):
        headings = self.soup.find_all(["h1", "h2", "h3"])

        all_headings = []
        
        for heading in headings:
            text = heading.get_text(strip=True)
            if text:
                all_headings.append(text)

        return all_headings
