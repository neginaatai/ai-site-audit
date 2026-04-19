from flask import Flask, render_template, request
import anthropic
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

def scrape_site(url):
    try:
        page = requests.get(url, timeout=10, verify=False)
        soup = BeautifulSoup(page.content, 'html.parser')
        meta_desc = soup.find("meta", {"name": "description"})
        return {
            "title": soup.title.string if soup.title else "None",
            "meta_description": meta_desc["content"] if meta_desc else "None",
            "h1_tags": [h.text for h in soup.find_all("h1")],
            "h2_tags": [h.text for h in soup.find_all("h2")],
            "links": len(soup.find_all("a")),
            "images": len(soup.find_all("img")),
            "images_without_alt": len([i for i in soup.find_all("img") if not i.get("alt")]),
            "word_count": len(soup.get_text().split())
        }
    except Exception as e:
        return {"error": str(e)}

def generate_audit(site_data, url):
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    prompt = f"""
    You are a professional web analyst. Analyze this website data and generate 
    a structured site assessment report.

    URL: {url}
    Site Data: {site_data}

    Generate a report with these exact sections:
    1. OVERALL SCORE (out of 100)
    2. SEO ANALYSIS (title, meta description, heading structure)
    3. CONTENT QUALITY (word count, structure, clarity)
    4. TECHNICAL HEALTH (images, links, alt tags)
    5. TOP 3 STRENGTHS
    6. TOP 3 CRITICAL ISSUES
    7. PRIORITY RECOMMENDATIONS (ranked 1-5)

    Be specific, actionable, and professional.
    """
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        site_data = scrape_site(url)
        audit = generate_audit(site_data, url)
        return render_template("report.html", audit=audit, url=url)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
