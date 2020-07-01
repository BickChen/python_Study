from wsgiref.simple_server import make_server
import re
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def book():
    data = '''
    <h1>欢迎来到撸猫专区</h1>

    <img src='/static/testimg.gif' />

    '''
    return data

def index():
    return 'index type!'

def imgs(url):
    print('____进入传输文件____')
    img_relative_path = re.sub("/static/", r'\\imgs\\', url, count=1)
    img_path = "%s%s"% (BASE_DIR, img_relative_path)
    print('img PATH:',img_path)
    if os.path.exists(img_path):
        f = open(img_path,'rb')
        data = f.read()
        f.close()
        print("拿到文件数据")
        return data
    else:
        return [bytes('404 not found.', encoding="utf-8")]

def url_dic():
    urls = {
        '/book': book,
        '/index': index
    }
    return urls

def run(env,conn):
    url_list = url_dic()
    cilent_url = env["PATH_INFO"]

    if cilent_url in url_list:
        conn('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
        return [bytes(url_list[cilent_url](),encoding='utf-8')]
    elif cilent_url.startswith('/static/'):
        img_data = imgs(cilent_url)
        conn('200 OK', [('Content-Type', 'text/jpg;charset=utf-8')])
        return [img_data,]
    else:
        conn('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
        return [bytes('404 not found.',encoding="utf-8")]


if __name__ in "__main__":
    httpd = make_server('localhost',8080,run)
    httpd.serve_forever()