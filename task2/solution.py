import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "https://ru.wikipedia.org"
START_URL = f"{BASE_URL}/wiki/Категория:Животные_по_алфавиту"

def parse_animals_count(max_pages=None):
    url = START_URL
    letter_counts = {}
    page_num = 0

    while url:
        print(f"Парсинг: {url}")
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        for item in soup.select(".mw-category-group"):
            title = item.find("h3")
            if not title:
                continue
            letter = title.text.strip()

            links = item.select("ul li")
            letter_counts[letter] = letter_counts.get(letter, 0) + len(links)

        page_num += 1
        if max_pages and page_num >= max_pages:
            break

        next_link = soup.find("a", text="Следующая страница")
        url = BASE_URL + next_link['href'] if next_link else None
        time.sleep(0.5)

    with open("task2/beasts.csv", "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for letter, count in sorted(letter_counts.items()):
            writer.writerow([letter, count])
