import requests
from bs4 import BeautifulSoup
import json
from email_utils import send_email

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

URL = config["url"]
KEYWORD = config["keyword"]

def scrape_and_notify():
    try:
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "html.parser")
        
        if KEYWORD.lower() in soup.get_text().lower():
            print("🔍 Keyword found! Sending email...")
            subject = f"Keyword Alert: {KEYWORD}"
            body = f"The keyword \"{KEYWORD}\" was found on {URL}"
            send_email(subject, body, config)
        else:
            print("⚠️ Keyword not found.")
    except Exception as e:
        print("❌ Error during scraping:", e)

if __name__ == "__main__":
    scrape_and_notify()
