import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)

data = response.text

soup = BeautifulSoup(data, "html.parser")

movies_name = soup.select(".article-title-description h3")
movies_list = [film.get_text() for film in movies_name]

movies_list.reverse()
with open("movies.txt", "w") as data_file:
    for row in range(100):
        data_file.write(
            f"{movies_list[row]}\n"
        )

print("Done")
