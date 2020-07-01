from wsgiref.simple_server import make_server

def book():
    return 'book type!'

def index():
    return 'index type!'

def url_dic():
    urls = {
        '/book': book,
        '/index': index
    }
    return urls

def run(env,conn):
    url_list = url_dic()
    cilent_url = env["PATH_INFO"]
    conn('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    if cilent_url in url_list:
        return [bytes(url_list[cilent_url](),encoding='utf-8')]
    else:
        return [bytes('404 not found.',encoding="utf-8")]


if __name__ in "__main__":
    httpd = make_server('localhost',8080,run)
    httpd.serve_forever()