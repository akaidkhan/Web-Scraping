import urllib.request
from bs4 import BeautifulSoup
address = "https://www.rottentomatoes.com/m/star_wars_the_rise_of_skywalker/reviews"

page= urllib.request.urlopen(address)

soup = BeautifulSoup(page,'html.parser')
#print(soup.prettify())

review = soup.find_all('div',attrs={'class':'the_review'})
#print(review)

for i in review:
    print("review:")
    print(i.get_text(),"\n")
