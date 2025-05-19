# Telco Web Scraper for GenAI Knowledge Base

This is a simple Python script that scrapes public telco websites (e.g. Maxis, Celcom, Digi, U Mobile, YES) and saves the cleaned text into `.txt` files. These files can then be uploaded to Amazon S3 for indexing into a GenAI Knowledge Base (Bedrock RAG).

---

## 🔧 Requirements

- Python 3.x
- Required libraries:
  - `requests`
  - `beautifulsoup4`

Install them using:

```bash
pip install requests beautifulsoup4
```

---

## 🚀 How to Use

1. Run the script:

```bash
python telco_scraper.py
```

2. You’ll see a list of telco websites to scrape.

3. Select the one you want by typing its number.

4. The scraped content will be saved into the `scraped_results/` folder.

Example:
```bash
scraped_results/maxis_postpaid_plans.txt
```

---

## 🪣 Next Step: Upload to S3

Once the `.txt` files are saved, you can manually upload them to your S3 bucket for use in your Bedrock Knowledge Base.

Example CLI upload:
```bash
aws s3 cp scraped_results/maxis_postpaid_plans.txt s3://your-bucket-name/knowledge-base/telco/
```

---

## 📌 Notes

- Script automatically removes headers, navbars, footers, scripts, etc.
- You can extend it to scrape multiple URLs or schedule it via cronjob/Lambda later.

---

## 💡 Use Case

Great for:
- Feeding real telco plan data into your GenAI chatbot
- Creating a telco comparison bot
- FAQ automation using Bedrock + RAG

---

## 👨‍💻 Created by

Amirul Afiq ✌️
