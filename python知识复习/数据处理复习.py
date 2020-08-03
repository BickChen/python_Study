api = input("股票查询接口>>: ")

def data(value, ):
    if type(value) is list:
        print(type(value))
    else:
        print(value)

if api.find('>') != -1:
    api_list = api.split('>')
    data(api_list)
elif api.find('<') != -1:
    api_list = api.split('<')
    data(api_list)
elif api.find('=') != -1:
    api_list = api.split('=')
    data(api_list)
else:
    data(api)