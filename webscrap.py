import requests
from bs4 import BeautifulSoup
import os

# 💡 Preset telco URLs
telco_urls = {
    "U Mobile - Postpaid Plans": "https://www.u.com.my/en/personal/postpaid",
    "U Mobile - Support": "https://www.u.com.my/en/support",

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
# 🧪 Run the scraper
# -------------------------------
if __name__ == "__main__":
    print("\nChoose a telco page to scrape:\n")

    for idx, name in enumerate(telco_urls.keys(), start=1):
        print(f"{idx}. {name}")

    choice = int(input("\nEnter your choice (e.g. 1): "))
    selected_name = list(telco_urls.keys())[choice - 1]
    selected_url = telco_urls[selected_name]

    filename = selected_name.lower().replace(" - ", "_").replace(" ", "_") + ".txt"

    print(f"\n[→] Scraping: {selected_name}")
    scrape_page_to_file(selected_url, filename)
