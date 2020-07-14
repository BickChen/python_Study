import requests
from lxml import etree
if __name__ in '__main__':
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    url = 'https://data.pentaq.com/GameDetail/7549/Game/13631?tour=76'
    data = requests.get(url=url, headers=headers).text
    with open('./LOL.html', 'w', encoding='utf-8') as fp:
        fp.write(data)
