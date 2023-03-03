import requests

from bs4 import BeautifulSoup


url="http://www.imdb.com/chart/top"

response=requests.get(url)



html_içeriği=response.content

soup=BeautifulSoup(html_içeriği,"html.parser")

movie_names=soup.find_all("td",{"class":"titleColumn"})

movie_rating=soup.find_all("td",{"class":"ratingColumn imdbRating"})


for movie, rating in zip(movie_names,movie_rating):
    movie = movie.text
    rating = rating.text

    movie = movie.strip()
    movie = movie.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")

    print("Movie",movie)
    print("Rating",rating)