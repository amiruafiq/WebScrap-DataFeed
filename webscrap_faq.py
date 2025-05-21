from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)
driver.get("https://www.u.com.my/en/personal/support/store-finder")
time.sleep(10)

faq_data = []

# Get all questions
questions = driver.find_elements(By.CSS_SELECTOR, "span.title")
print(f"🟡 Found {len(questions)} FAQ titles")

for i in range(len(questions)):
    try:
        # Re-fetch question list every time (avoid stale)
        current_questions = driver.find_elements(By.CSS_SELECTOR, "span.title")
        question = current_questions[i]
        question_text = question.text.strip()

        # Click and wait
        driver.execute_script("arguments[0].scrollIntoView();", question)
        driver.execute_script("arguments[0].click();", question)
        time.sleep(1)

        # Use XPath: find <p> inside the same accordion section
        p_xpath = f"(//accordion)[{i+1}]//div[contains(@class, 'text-component')]//p"
        answer_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, p_xpath))
        )
        answer_text = answer_element.text.strip()

        if question_text and answer_text:
            faq_data.append({
                "question": question_text,
                "answer": answer_text
            })

    except Exception as e:
        print(f"❌ Skipped one at index {i}: {e}")

# Save to JSON
with open("u_mobile_faq.json", "w", encoding="utf-8") as f:
    json.dump(faq_data, f, indent=2, ensure_ascii=False)

print(f"✅ Done! {len(faq_data)} FAQs saved to u_mobile_faq.json")
driver.quit()
