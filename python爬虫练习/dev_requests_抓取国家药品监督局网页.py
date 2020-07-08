import requests, json

if __name__ in '__main__':
    url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'

    haders = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }

    url_data = {
        'on': 'true',
        'page': '1',
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
    }

    response = requests.post(url=url, data=url_data, headers=haders).text
    print(response)
    response_dic = json.loads(response)
    response_list = response_dic['list']
    # print(response_dic['list'][0])
    with open('./data.json', 'w+') as fp:
        for i in response_list:
            url_id = i['ID']
            url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
            data = {
                'id': url_id
            }

            response = requests.post(url=url, data=data, headers=haders).json()
            json.dump(response, fp=fp, ensure_ascii=False)
    print('end !')