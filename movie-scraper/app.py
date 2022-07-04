from bs4 import BeautifulSoup
import requests
import random

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

c = soup.find_all("td", class_="titleColumn")


def print_top_250():
    for i, a in enumerate(c):
        movieTitle = a.find("a")
        print(i, movieTitle.contents[0])


def find_movie_to_watch():
    movieList = []
    for a in c:
        movieTitle = a.find("a")
        movieList.append(movieTitle.contents[0])
    # generate a random # between 0 and 249
    i = random.randint(0, 249)
    print("you should watch ->", movieList[i])
find_movie_to_watch()