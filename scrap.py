import csv
import bs4
import requests
from fake_useragent import UserAgent


with open('c2x.csv',encoding="utf-8",newline ='') as f:
  lines = csv.reader(f)
  data_trivial = list(lines)


data = []

only_alpha = ""

for i in data_trivial:
    data.append(str(i))

data_final = []

for i in data:
    for char in i:
        if ord(char) >= 65 and ord(char) <= 90:
            only_alpha += char
        elif ord(char) >= 97 and ord(char) <= 122:
            only_alpha += char
    data_final.append(only_alpha)


ua = UserAgent()

city = []
text = []
urls = []
name = []


for i in data:
    only = ""
    for char in i:
        if ord(char) >= 65 and ord(char) <= 90:
            only += char
        elif ord(char) >= 97 and ord(char) <= 122:
            only += char
    url = "https://www.holidify.com/places/" + only + "/sightseeing-and-things-to-do.html"
    page = requests.get(url, headers={"user-agent": ua.chrome})
    html = page.content
    soup = bs4.BeautifulSoup(html, "html.parser")
    print("Fetching Data of",only,);
    for a in soup.findAll('h3',attrs={'class':'card-heading'}):
        x = str(a.text).split('. ')
        name.append(x[1])
        city.append(only)
    for a in soup.findAll('p',attrs={'class':'card-text'}):
        x = str(a.text)
        text.append(x)
    for a in soup.findAll('img',attrs={'class':'card-img-top lazy'}):
        x = str(a.get('data-original'))
        urls.append(x)

sheet = []

for i in range(len(name)):
    row = []
    row.append(name[i])
    row.append(city[i])
    row.append(text[i])
    row.append(urls[i])
    sheet.append(row)



with open('db_final.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(sheet)
