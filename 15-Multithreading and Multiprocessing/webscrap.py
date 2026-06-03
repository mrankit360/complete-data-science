import threading
import requests
from bs4 import BeautifulSoup

urls=[

'https://python.langchain.com/v0.2/docs/introduction/',

'https://python.langchain.com/v0.2/docs/concepts/',

'https://python.langchain.com/v0.2/docs/tutorials/'

]

def fetch_urls(url):
    response = requests.get(url)
    bs = BeautifulSoup(response.content, 'html.parser')
    print(f'fetched {len(bs.text)} character from {url}')

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_urls,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('Everything is fetched')
