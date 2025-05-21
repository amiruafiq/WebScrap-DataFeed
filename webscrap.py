import requests
from bs4 import BeautifulSoup
import os

# 💡 Preset telco URLs
telco_urls = {
    "U Mobile - TradeIn": "https://www.u.com.my/en/personal/devices/trade-in",
}

def scrape_page_to_file(url, output_filename="output.txt", output_folder="scraped_results"):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"[✗] Failed to fetch {url} (status code {response.status_code})")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "footer", "nav", "header", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator="\n", strip=True)
    os.makedirs(output_folder, exist_ok=True)

    file_path = os.path.join(output_folder, output_filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"[✓] Scraped content saved to: {file_path}")


# -------------------------------
# 🚀 Auto-run all URLs
# -------------------------------
if __name__ == "__main__":
    print("\n[🔄] Scraping all U Mobile pages...\n")

    for name, url in telco_urls.items():
        filename = name.lower().replace(" - ", "_").replace(" ", "_") + ".txt"
        print(f"[→] Scraping: {name}")
        scrape_page_to_file(url, filename)

    print("\n[✅] All pages scraped and saved to 'scraped_results/' folder.")
