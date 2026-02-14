import requests
import bs4

class Wordle:
    """Tools for retrieving data from New York Times games."""
    
    @property
    def answer(self):
        """Retrieves the answer for today's Wordle."""
        link = "https://www.tomsguide.com/news/what-is-todays-wordle-answer"
        req = requests.get(link)
        soup = bs4.BeautifulSoup(req.text, "html.parser")
        word = soup.find_all("strong")[7].text
        word = word.upper().replace(".", "")
        return word
