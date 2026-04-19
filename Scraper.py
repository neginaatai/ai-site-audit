import requests
from bs4 import BeautifulSoup

def scrape_site(url):
    page = requests.get(url, timeout=10)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    return {
        "title": soup.title.string if soup.title else "None",
        "meta_description": soup.find("meta", {"name": "description"}),
        "h1_tags": [h.text for h in soup.find_all("h1")],
        "h2_tags": [h.text for h in soup.find_all("h2")],
        "links": len(soup.find_all("a")),
        "images": len(soup.find_all("img")),
        "images_without_alt": len([i for i in soup.find_all("img") if not i.get("alt")]),
        "word_count": len(soup.get_text().split())
    }
