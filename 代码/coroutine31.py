#!/usr/bin/env python3

import asyncio
import sys

#指定服务器绑定的IP地址。
host = '127.0.0.1'
#指定服务器监听的TCP端口。
port = 8000


#定义处理连接请求的协程函数。
async def echo(reader, writer):
    #在TCP连接成功建立后，可以一直响应客户发来的消息，并将消息反射给客户，直到收到特殊
    # 消息“quit”。
    while True:
        #异步读取一行二进制数据，注意这会包含\n。
        data = await reader.readline()
        #将二进制数据转换为文本消息。
        msg = data.decode()
        #将文本消息再次转换为二进制数据。
        data = msg.encode()
        #将二进制数据原封不动地异步写入。
        writer.write(data)
        #如果读取到的文本消息是“quit”，则退出循环。
        if msg == "quit\n":
            break
    #关闭异步流。
    writer.close()


async def main():
    #创建服务器，并绑定到指定的IP，在指定的TCP端口上监听。  服务器被创建后并未启动。
    server = await asyncio.start_server(echo, host, port, start_serving=False)
    #创建服务器的控制任务。
    controller = asyncio.create_task(server.serve_forever())
    try:
        #启动并运行服务器60秒。
        await asyncio.wait_for(controller, 60)
    except asyncio.TimeoutError:
        #60秒后自动关闭服务器。
        controller.cancel()
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
