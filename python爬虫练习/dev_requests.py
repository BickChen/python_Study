# -*- coding:utf-8 -*-

import requests

if __name__ in "__main__":
    url = 'https://www.sogou.com/web'
    param = {
        'query': '小猿圈'
    }
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }

    response = requests.get(url=url, params=param, headers=headers)
    url_data = response.text
    print(url_data)

    with open('./' + param['query'] + '.html', 'w', encoding='utf-8') as fp:
         fp.write(url_data)
