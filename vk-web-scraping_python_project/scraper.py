import requests
from bs4 import BeautifulSoup
import webbrowser  # This is a built-in module, no need to install

url = "https://www.youtube.com/watch?v=Zdcth9NndEA"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a', href=True):
    absolute_url = link['href']
    if absolute_url.startswith('http'):
        print(absolute_url)
        webbrowser.open_new_tab(absolute_url)
