import requests, json, time, random

if __name__ == '__main__':
    url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    with open('./data', 'a') as file:
        for i in range(1,352):
            url_keys = {
                'on':' true',
                'page': i,
                'pageSize': '15',
                'productName': '',
                'conditionType': '1',
                'applyname': '',
                'applysn': '',
            }
            reque = requests.post(url=url, data=url_keys, headers=headers)
            data = reque.text
            # print(data)
            dic_data = json.loads(data)
            time.sleep(random.randint(1,10))
            print(i)
            list_data = dic_data['list']
            for d in list_data:
                str_d = str(d) + '\n'
                file.write(str_d)
    print('写入完毕！')
            # json_data = json.dumps(data, ensure_ascii=False)
            # fp = open('./data.json', 'w', encoding='utf-8')
            # json.dump(json_data, fp=fp, ensure_ascii=False)