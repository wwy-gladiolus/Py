#!/usr/bin/env python3

import asyncio
import sys

host = '127.0.0.1'
port = 8001


async def main():
    reader, writer = await asyncio.open_connection(host, port)
    while True:
        text = input('Input a "(command, message)" style request, "(quit,)" to stop: ')
        #将文本数据转换为二进制数据，不需要添加\n。
        data = text.encode()
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
