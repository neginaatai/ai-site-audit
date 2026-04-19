# AI Site Audit Generator

An autonomous web application that takes any website URL and generates a comprehensive AI-powered audit report using Claude AI and Flask.

## What It Does

- Scrapes any website URL automatically
- Analyzes SEO, content quality, and technical health
- Generates a structured audit report powered by Claude AI including:
  - Overall score out of 100
  - SEO analysis with detailed breakdown
  - Content quality metrics
  - Technical health assessment
  - Top 3 strengths and critical issues
  - Priority recommendations with timelines

## Tech Stack

- Python / Flask
- BeautifulSoup4 (web scraping)
- Anthropic Claude API (AI analysis)
- HTML/CSS (frontend)

## Setup

```bash
git clone https://github.com/neginaatai/ai-site-audit.git
cd ai-site-audit
python3 -m venv venv
source venv/bin/activate
pip install flask anthropic beautifulsoup4 requests
export ANTHROPIC_API_KEY="your-key-here"
python3 FlaskAPP.py
```

Open `http://127.0.0.1:5001` in your browser.

## Demo

Enter any website URL → receive a full AI-generated audit report in seconds.

Built by Negina Atai
