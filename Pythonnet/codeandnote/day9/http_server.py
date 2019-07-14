"""
HTTP Server 2.0
"""

from socket import *
from threading import Thread
import sys


# 封装HTTP类作为一个完整的服务功能
class HTTPServer(object):
    def __init__(self, server_addr, static_dir):
        # 属性添加
        self.server_address = server_addr
        self.static_dir = static_dir
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, \
                               SO_REUSEADDR, 1)

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.server_address)
        self.ip = self.server_address[0]
        self.port = self.server_address[1]

    # 启动服务
    def serve_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %d" % self.port)
        while True:
            try:
                connfd, addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("退出服务器")
            except Exception as e:
                print(e)
                continue
            # 创建新的线程处理请求
            th = Thread(target=self.handle, \
                        args=(connfd,))
            th.setDaemon(True)
            th.start()

    # 处理浏览器请求
    def handle(self, connfd):
        # 接收HTTP请求
        request = connfd.recv(4096)

        # 防止异常断开
        if not request:
            return

        # 请求解析
        requestHeaders = request.splitlines()
        print(connfd.getpeername(), ':', \
              requestHeaders[0])

        # 获取请求内容
        getRequest = str(requestHeaders[0]).split(' ')[1]

        if getRequest == '/' or getRequest[-5:] == '.html':
            self.get_html(connfd, getRequest)
        else:
            # 　其他内容
            self.get_data(connfd, getRequest)

    def get_html(self, connfd, getRequest):
        if getRequest == '/':
            filename = self.static_dir + '/index0.html'
        else:
            filename = self.static_dir + getRequest

        try:
            f = open(filename)
        except IOError:
            # 没有这个网页
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += '\r\n'
            responseBody = "Sorry,Not found the page"
        else:
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += '\r\n'
            responseBody = f.read()
        finally:
            response = responseHeaders + responseBody
            connfd.send(response.encode())

    def get_data(self, connfd, getRequest):
        data = "HTTP/1.1 200 OK\r\n\r\n<p>Waiting httpserver v3.0</p>"
        connfd.send(data.encode())


if __name__ == "__main__":
    # 使用者想用http类干什么?
    # 启动服务，用于展示我的一些静态网页
    # 什么需要用户提供?
    # 服务端地址和网页
    # 用户怎么用这个http类?
    server_addr = ('0.0.0.0', 8000)  # 服务地址
    statis_dir = "./static"  # 网页存放位置
    # 生成服务器对象
    httpd = HTTPServer(server_addr, statis_dir)
    # 启动服务
    httpd.serve_forever()
