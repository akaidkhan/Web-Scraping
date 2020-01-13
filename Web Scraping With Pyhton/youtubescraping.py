import bs4
import requests

url = "https://www.youtube.com/channel/UCa5UDzFzpIjJ1VSxCSlQP_g/videos"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
for link in soup.find_all('a'):
    link = link.get("href")
    if link[0:3]=="/wa":
        print("https://www.youtube.com/"+ link)

        
