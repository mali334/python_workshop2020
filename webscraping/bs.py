from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import csv
session = HTMLSession()


urls = []
for i in range(1,51):
    urls.append(f"http://books.toscrape.com/catalogue/page-{i}.html")


csv_file=open("book.csv", "w")
csv_writer= csv.writer(csv_file,lineterminator="\n")

csv_writer.writerow(["Title","Price","ImageUrl"])
count = 1
for url in urls:
    source = session.get(url).html.html
    soup = BeautifulSoup(source, "lxml")

    box = soup.find("ol")
    elements = box.find_all("li")
    title = []
    picture = []
    cost = []
    for element in elements:
        name = element.select("h3 a")[0]["title"]
        title.append(name)
        image = element.select("img")[0]["src"]
        image_url = r"http://books.toscrape.com/"+image
        picture.append(image_url)
        price = element.find("p",class_="price_color").text
        cost.append(price)
        csv_writer.writerow([name, price, image_url])
        print(count, end=" ")
        count +=1

csv_file.close()
