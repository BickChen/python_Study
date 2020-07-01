from wsgiref.simple_server import make_server

def run(env,coon):
    print(env)
    coon('200 OK',[('Content-Type', 'text/html;charset=utf-8')])
    return [bytes("<h1>Hi Yasin</h1>",encoding='utf-8')]

if __name__ in "__main__":
    httpd = make_server('localhost',8080,run)
    httpd.serve_forever()

