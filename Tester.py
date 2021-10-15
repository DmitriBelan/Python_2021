import requests
from bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
url = 'https://www.google.com/search?q=rur+to+eur&oq=rur+to+eur&aqs=chrome..69i57j0i10l9.2158j1j7&sourceid=chrome&ie=UTF-8'
r = requests.get(url, headers=headers)
soup = BS(r.content, 'html.parser')
price = float(soup.find('span', class_='DFlfde SwHCTb')['data-value'])
print(float(user_input)/price)


