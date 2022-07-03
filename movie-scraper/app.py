
from bs4 import BeautifulSoup
import requests
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

c = soup.find_all("td", class_="titleColumn")

#print the top 250 movies on IMDB
for i, a in enumerate(c):
  movieTitle = a.find("a")
  print(i, movieTitle.contents[0])
