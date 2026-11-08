import requests
from bs4 import BeautifulSoup
import json


url = "https://guide.herzen.spb.ru/schedule/25368/by-dates"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()

subject = "Алгоритмизация вычислительных процессов"
index = text.find(subject)

days = soup.find_all("div", class_ = "p-5 mt-5 rounded-lg border border-gray-100 bg-gray-200")



all_lessons = []
for day in days:
    lines = list(day.stripped_strings)
    for i, line in enumerate(lines):
            lesson = {}
            if ":" in line and "-" in line:
                if "Подгруппа" in lines[i+1]:
                    date = lines[0]
                    lesson["date"] = date
                    lesson["time"] = line
                    lesson["lesson"] = lines[i+2]
                    lesson["teacher"] = lines[i+6]
                    lesson["room"] = lines[i+7]
                else:
                    date = lines[0]
                    lesson["date"] = date
                    lesson["time"] = line
                    lesson["lesson"] = lines[i+1]
                    lesson["teacher"] = lines[i+5]
                    lesson["room"] = lines[i+6]
                all_lessons.append(lesson)

print(len(all_lessons))
with open(
    "schedule.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        all_lessons,
        file,
        ensure_ascii=False,
        indent=4
    )
print(len(all_lessons))
print(all_lessons[0])
print(all_lessons[-1])