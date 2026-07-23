import re
import requests
from bs4 import BeautifulSoup

def fetch_page_html(url):
    """Fetches the raw HTML content of a public URL."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.text
        return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_business_info(html_content):
    """Parses HTML to find business data and social media hooks."""
    if not html_content:
        return {}

    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract Business Title (looks for standard heading tags)
    title_tag = soup.find('h1') or soup.find('title')
    business_name = title_tag.text.strip() if title_tag else "Unknown Business"

    # Extract Public Web Links
    links = []
    for anchor in soup.find_all('a', href=True):
        links.append(anchor['href'])

    # Filter out Instagram profiles found on the page
    instagram_links = [link for link in links if "instagram.com" in link]
    instagram_handle = instagram_links[0] if instagram_links else "Not Found"

    # Filter out external company websites (ignoring self-links or common search engines)
    company_website = "Not Found"
    for link in links:
        if "http" in link and not any(domain in link for domain in ["google.com", "instagram.com", "facebook.com"]):
            company_website = link
            break

    return {
        "Business Name": business_name,
        "Website": company_website,
        "Instagram Link": instagram_handle
    }
