import requests
from bs4 import BeautifulSoup
import json

def scrape_website(url):
    """Scrape the given website and store content for chatbot usage."""
    headers = {'User-Agent': 'Mozilla/5.0'}  # Prevents getting blocked
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract structured content
        title = soup.title.string if soup.title else "No title found"
        headings = [h.get_text(strip=True) for h in soup.find_all("h1")]
        paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]

        scraped_data = {
            "url": url,
            "title": title,
            "headings": headings[:5],  # First 5 headings
            "content": " ".join(paragraphs[:10])  # First 10 paragraphs
        }

        # Save as JSON
        with open("scraped_data.json", "w", encoding="utf-8") as file:
            json.dump(scraped_data, file, indent=4)

        return scraped_data

    except Exception as e:
        return {"error": f"Scraping failed: {e}"}

# Run Scraper
if __name__ == "__main__":
    user_url = input("🌍 Enter website URL to scrape: ")
    result = scrape_website(user_url)
    print("✅ Scraping complete. Data saved in 'scraped_data.json'.")
