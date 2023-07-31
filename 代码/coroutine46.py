#!/usr/bin/env python3
#改写自coroutine33.py

import asyncio
import sys

host = '127.0.0.1'
port = 8001


async def engine(reader, writer):
    while True:
        binary = await reader.readuntil(b")")
        text = binary.decode().strip()
        command, _, message = text.partition(",")
        command = command.strip("( ")
        message = message.strip(") ")
        match command.lower():
            case "upper":
                message = message.upper()
            case "lower":
                message = message.lower()
            case "swapcase":
                message = message.swapcase()
            case "capitalize":
                message = message.capitalize()
            case "title":
                message = message.title()
            case "quit":
                message = "quit"
            case _:
                message = "unknown command."
        text = message + "\n"
        binary = text.encode()
        writer.write(binary)
        if message == "quit":
            break
    writer.close()


async def main():
    server = await asyncio.start_server(engine, host, port)
    #将Server对象当成异步上下文管理器来使用。
    async with server:
        await asyncio.sleep(60)


if __name__ == '__main__':
    asyncio.run(main())
