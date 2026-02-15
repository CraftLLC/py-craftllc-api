import requests
import bs4
from urllib.parse import quote as url

class UnknownMethod(Exception):
    """Exception for unknown HTTP methods."""
    pass

class ReqTools:
    """A set of tools for performing HTTP requests and parsing web pages."""

    def __init__(self):
        """Initializes a ReqTools instance."""
        pass
     
    def whois(self, address):
        """
        Retrieves WHOIS information for a specified IP address or domain.

        :param address: IP address or domain.
        :return: Dictionary with WHOIS data.
        """
        address = url(address)
        r = requests.get(f"https://who.is/whois-ip/ip-address/{address}")
        soup = bs4.BeautifulSoup(r.text, "html.parser")
        text = soup.find("pre").text
        text_lines = text.splitlines()
        toReturn = {}
        for text in text_lines:
            option = text[:15].replace(" ", "").replace(":", "").strip()
            value = text[15:]
            toReturn[option] = value
        try:
            del toReturn["Comment"]
        except:
            pass
        return toReturn

    def find_all_images_url(self, site_url, method="GET", **kwargs):
        """Finds all image URLs on the specified site."""
        if method.upper() == "GET":
            req = requests.get(site_url, **kwargs)
        elif method.upper() == "POST":
            req = requests.post(site_url, **kwargs)
        elif method.upper() == "PUT":
            req = requests.put(site_url, **kwargs)
        elif method.upper() == "DELETE":
            req = requests.delete(site_url, **kwargs)
        elif method.upper() == "PATCH":
            req = requests.patch(site_url, **kwargs)
        elif method.upper() == "OPTIONS":
            req = requests.options(site_url, **kwargs)
        elif method.upper() == "HEAD":
            req = requests.head(site_url, **kwargs)
        elif method.upper() == "TRACE":
            req = requests.trace(site_url, **kwargs)
        else:
            raise UnknownMethod("Please input correct HTTP method.")

        req.raise_for_status()

        if method.upper() == "OPTIONS":
            return req.headers

        soup = bs4.BeautifulSoup(req.text, "html.parser")
        images_urls = []
        images = soup.find_all("img")

        for img in images:
            src = img.get("src")
            if src:
                if src.startswith("/"):
                    src = f"{site_url}{src}"
                images_urls.append(src)

        return images_urls

    def get_page_title(self, site_url):
        """Gets the page title."""
        req = requests.get(site_url)
        req.raise_for_status()
        soup = bs4.BeautifulSoup(req.text, "html.parser")
        return soup.title.string.strip() if soup.title else "No title found"

    def get_all_links(self, site_url):
        """Gets all links on the page."""
        req = requests.get(site_url)
        req.raise_for_status()
        soup = bs4.BeautifulSoup(req.text, "html.parser")
        links = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if href.startswith("/"):
                href = f"{site_url}{href}"
            links.append(href)
        return links

    def check_http_status(self, site_url):
        """Checks the HTTP status code for the specified site."""
        try:
            req = requests.get(site_url)
            return req.status_code
        except requests.exceptions.RequestException as e:
            return f"Error: {e}"

    def extract_paragraphs(self, site_url):
        """Extracts all paragraphs from the specified site."""
        req = requests.get(site_url)
        req.raise_for_status()
        soup = bs4.BeautifulSoup(req.text, "html.parser")
        paragraphs = [p.get_text() for p in soup.find_all("p")]
        return paragraphs

    def get_meta_tags(self, site_url):
        """Gets all meta tags from a web page."""
        req = requests.get(site_url)
        req.raise_for_status()
        soup = bs4.BeautifulSoup(req.text, "html.parser")
        meta_tags = {meta.get("name"): meta.get("content") for meta in soup.find_all("meta") if meta.get("name")}
        return meta_tags

    def check_ssl_certificate(self, site_url):
        """Checks the SSL certificate for HTTPS connections."""
        try:
            req = requests.get(site_url)
            if req.url.startswith("https"):
                return "SSL certificate is valid."
            else:
                return "SSL certificate is not valid."
        except requests.exceptions.SSLError as e:
            return f"SSL error: {e}"
        except requests.exceptions.RequestException as e:
            return f"Error: {e}"

    def save_html_to_file(self, site_url, filename="output.html"):
        """Saves the page's HTML code to a file."""
        req = requests.get(site_url)
        req.raise_for_status()
        with open(filename, "w", encoding="utf-8") as file:
            file.write(req.text)
        return f"HTML content saved to {filename}"

    def extract_list_items(self, site_url):
        """Extracts all list items from a web page."""
        req = requests.get(site_url)
        req.raise_for_status()
        soup = bs4.BeautifulSoup(req.text, "html.parser")
        list_items = [li.get_text() for li in soup.find_all("li")]
        return list_items

    def get_first_h1(self, site_url):
        """Gets the first &lt;h1&gt; header from a web page."""
        req = requests.get(site_url)
        req.raise_for_status()
        soup = bs4.BeautifulSoup(req.text, "html.parser")
        h1 = soup.find("h1")
        return h1.get_text().strip() if h1 else "No <h1> tag found"

    def get_all_scripts(self, site_url):
        """Gets all script sources from a web page."""
        req = requests.get(site_url)
        req.raise_for_status()
        soup = bs4.BeautifulSoup(req.text, "html.parser")
        scripts = [script.get("src") for script in soup.find_all("script") if script.get("src")]
        return scripts

    def extract_form_data(self, site_url):
        """Extracts form data from a web page."""
        req = requests.get(site_url)
        req.raise_for_status()
        soup = bs4.BeautifulSoup(req.text, "html.parser")
        forms = []
        for form in soup.find_all("form"):
            action = form.get("action")
            method = form.get("method", "GET").upper()
            inputs = {input.get("name"): input.get("type") for input in form.find_all("input")}
            forms.append({"action": action, "method": method, "inputs": inputs})
        return forms

    def get_css_links(self, site_url):
        """Gets all CSS file links from a web page."""
        req = requests.get(site_url)
        req.raise_for_status()
        soup = bs4.BeautifulSoup(req.text, "html.parser")
        css_links = [link.get("href") for link in soup.find_all("link", rel="stylesheet")]
        return css_links
