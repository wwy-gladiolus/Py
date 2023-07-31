#!/usr/bin/env python3

import asyncio
import sys

#指定实现Unix套接字的文件。
path = "unix_socks/temporary.sock"


async def main():
    #建立到服务器的Unix套接字连接，并获得相关异步流的读取器和写入器。
    reader, writer = await asyncio.open_unix_connection(path)
    while True:
        text = input('You can send any message to the server, "quit" to stop: ')
        msg = text + "\n"
        data = msg.encode()
        writer.write(data)
        data = await reader.readline()
        msg = data.decode()
        print(msg)
        if msg == "quit\n":
            break
    writer.close()
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
