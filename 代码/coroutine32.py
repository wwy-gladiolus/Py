#!/usr/bin/env python3

import asyncio
import sys

#指定服务器的IP地址。
host = '127.0.0.1'
#指定服务器的TCP端口。
port = 8000


async def main():
    #建立到服务器的TCP连接，并获得相关异步流的读取器和写入器。
    reader, writer = await asyncio.open_connection(host, port)
    #在TCP连接成功建立后，可以一直向服务器发送消息，并将反射来的消息通过标准输出显示，
    # 直到发送了特殊消息“quit”。
    while True:
        #让用户随意输入一行文本，注意这不会包含\n。
        text = input('You can send any message to the server, "quit" to stop: ')
        #给文本添加\n以形成文本消息。
        msg = text + "\n"
        #将文本消息转换为二进制数据。
        data = msg.encode()
        #将二进制数据异步写入。
        writer.write(data)
        #异步读取一行二进制数据，注意这会包含\n。
        data = await reader.readline()
        #将二进制数据转换为文本消息。
        msg = data.decode()
        #显示文本消息。
        print(msg)
        #如果读取到的文本消息是“quit”，则退出循环。
        if msg == "quit\n":
            break
    #关闭异步流。
    writer.close()
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
