import requests, json
if __name__ == '__main__':
    post_url = 'https://fanyi.baidu.com/sug'
    url_data = {
        'kw': 'dog'
    }
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    response = requests.post(url=post_url, data=url_data, headers=headers)
    date = response.json()
    print(date)
    fp = open('./dog.json', 'w', encoding='utf-8')
    json.dump(date, fp=fp, ensure_ascii=False)

    # with open('./'+url_data['kw']+'.html','w',encoding='utf-8') as fp:
