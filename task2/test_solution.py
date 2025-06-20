import os
from solution import parse_animals_count

def test_beasts_csv_created_fast():
    parse_animals_count(max_pages=2)
    assert os.path.exists("task2/beasts.csv")
    with open("task2/beasts.csv", encoding="utf-8") as f:
        content = f.read()
        assert any(letter in content for letter in ["А,", "Б,", "В,"])
