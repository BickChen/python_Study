import requests

if __name__ in '__main__':
    url = 'https://www.tianyancha.com/company/593822322'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }

    data = requests.get(url=url, headers=headers).text
    with open('./tian.html', 'w') as fp:
        fp.write(data)
    print('end !')