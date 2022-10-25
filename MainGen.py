from bs4 import BeautifulSoup as bs
import requests as rqst
from googlesearch import search
import os

links = []
progress = 0

query = input("What do you want info on: ")
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    os.system("cls")
    progress += 10
    print(progress, "%")
    links.append(j)


url = links[0]

bl = 0

# while "wikipedia" in links[bl]:
#     bl += 1
#     url = links[bl]

page = rqst.get(url)
soup = bs(page.content, "html.parser")

results = soup.find()
print(results.text)