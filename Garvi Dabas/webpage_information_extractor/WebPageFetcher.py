import requests
import bs4

class WebPageFetcher:

    def __init__(self, url):
        # Store the URL that will be used to fetch the webpage.
        self.url = url

    def fetch_page(self):
        # Fetch the webpage, check the response, and return a parsed BeautifulSoup object.
        try:

            response = requests.get(self.url, timeout=10)
            response.raise_for_status()

            # Parse the HTML response into a BeautifulSoup object for extraction.
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            return soup

        # Handle cases where a URL is required but was not provided.
        except requests.exceptions.URLRequired:
            print(
                "\nA URL was required but not provided.\n"
                )

        # Handle URLs with an unsupported or invalid scheme.
        except requests.exceptions.InvalidURL:
            print(
                "\nThe URL has  scheme/protocol, but that scheme is not supported.\n"
                "Please enter a valid URL.\n"
                )

        # Handle URLs that do not contain a scheme such as http:// or https://.
        except requests.exceptions.MissingSchema:
            print(
                "\nThe URL you entered does not contain scheme.\n"
                "Please enter a valid URL.\n"
                )
            
        # Handle URLs with a scheme that requests does not understand.
        except requests.exceptions.InvalidSchema:
            print(
                "\nThe scheme used in the URL is not valid.\n"
                "Please enter a valid URL.\n"
                )
            
        # Handle requests that take too long to receive a response.
        except requests.exceptions.Timeout:
            print(
                "\nRequest timed out. The server is taking too long to respond.\n"
                )

        # Handle failures when a connection to the server cannot be established.
        except requests.exceptions.ConnectionError:
            print(
                "\nConnection Error: Could not connect to the Server.\n"
                )

        # Handle HTTP error responses such as 404, 401, 403, and 500.
        except requests.exceptions.HTTPError as error:
            status = error.response.status_code

            if status == 404:
                print("\nResource not found.\n")

            elif status == 401:
                print("\nAuthentication Required.\n")

            elif status == 403:
                print("\nAccess forbidden.\n")

            elif status == 500:
                print("\nInternal Server Error.\n")

            else:
                print(f"\nHttp Error: {status}\n")

        # Handle any other request-related errors.
        except requests.exceptions.RequestException:
            print(
                "\nRequest failed.\n"
                )

        return None
        


