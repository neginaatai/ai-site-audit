import anthropic

def generate_audit(site_data, url):
    client = anthropic.Anthropic()
    
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
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return message.content[0].text