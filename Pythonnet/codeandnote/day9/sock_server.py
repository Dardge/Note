"""
通过 socketserver 模块完成网络并发
"""

from socketserver import *

# 创建tcp多进程并发
class Server(ThreadingMixIn, TCPServer):
    pass

# 具体请求处理
class Handler(StreamRequestHandler):
    # 重写方法
    def handle(self):
        print("Connect from:",self.client_address)
        while True:
            # self.request ==> accept->connfd
            data = self.request.recv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send(b'OK')

# 创建服务器对象
serv = Server(('0.0.0.0',8888),Handler)
serv.serve_forever()  # 启动服务
