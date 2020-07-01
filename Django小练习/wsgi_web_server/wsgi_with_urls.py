from wsgiref.simple_server import make_server

def book(env,conn):
    print("客户端访问了 book站点！")
    conn('200 OK',[('Content-Type', 'text/html;charset=utf-8')])
    return [bytes("<h1>book type! </h1>",encoding='utf-8')]

def index(env,conn):
    print("客户端访问了 index站点！")
    conn('200 OK',[('Content-Type', 'text/html;charset=utf-8')])
    return [bytes("<h1>index type! </h1>",encoding='utf-8')]

def url_dic():
    urls = {
        '/book': book,
        '/index': index
    }
    return urls

def run(env,conn):
    url_list = url_dic()
    cilent_url = env["PATH_INFO"]
    print(cilent_url)
    if cilent_url in url_list:
        func = url_list[cilent_url](env,conn)
        return func
    else:
        print('404')
        conn('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
        return [bytes("<h1>404 not found.</h1>",encoding='utf-8')]

if __name__ in "__main__":
    httpd = make_server('localhost',8080,run)
    httpd.serve_forever()

