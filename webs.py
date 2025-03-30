import requests
from bs4 import BeautifulSoup

page = requests.get("http://web.mta.info/developers/turnstile.html"); 
soup = BeautifulSoup(page.text, "html.parser")
links = soup.findAll("a")
#print(links)
i=36
while i<len(links):
    print(links[i])
    i = i+1

