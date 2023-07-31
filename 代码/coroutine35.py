#!/usr/bin/env python3

import asyncio
import sys

#指定实现Unix套接字的文件。
path = "unix_socks/temporary.sock"


async def echo(reader, writer):
    while True:
        data = await reader.readline()
        msg = data.decode()
        data = msg.encode()
        writer.write(data)
        if msg == "quit\n":
            break
    writer.close()


async def main():
    #创建服务器，并指定使用的Unix套接字。
    server = await asyncio.start_unix_server(echo, path, start_serving=False)
    controller = asyncio.create_task(server.serve_forever())
    try:
        await asyncio.wait_for(controller, 60)
    except asyncio.TimeoutError:
        controller.cancel()
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
