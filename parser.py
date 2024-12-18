import requests
from bs4 import BeautifulSoup
url = 'http://www.mingpao.com'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    page_title = soup.title.string
    print('Page Title:',page_title)
    for link in soup.find_all('a'):
        print(link.get('href'))
else:
    print(f"Failed to retrieve the webpage. Status code:{response.status_code}")
