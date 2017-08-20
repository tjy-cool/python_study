from wsgiref.simple_server import make_server

def f1():
    return "F1"
def f2():
    return "F2"
def f3():
    return "F3"
routers = {
    "/index/": f1,
    "/news/": f2,
    "/home/": f3
}

def RunServer(environ, start_response):
    start_response("200 OK", [('Content-Type', 'text/html')])
    # return '<h1>Hello, web!</h1>'
    url = environ['PATH_INFO']
    if url in routers.keys():
        func_name = routers[url]
        return func_name()

    else:
        return "404"

if __name__ == "__main__":
    httpd = make_server("", 8000, RunServer)
    print("Serving HTTP on port 8000...")
    # while循环，等到用户请求到来
    # 只要有请求进来，执行RunServer函数
    httpd.serve_forever()
