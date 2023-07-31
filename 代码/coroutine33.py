#!/usr/bin/env python3

import asyncio
import sys

host = '127.0.0.1'
port = 8001


async def engine(reader, writer):
    while True:
        #从异步流读取“(command, message)”格式的二进制数据。
        binary = await reader.readuntil(b")")
        #将二进制数据转换为文本数据。
        text = binary.decode().strip()
        #从文本数据中抽取命令和消息。
        command, _, message = text.partition(",")
        command = command.strip("( ")
        message = message.strip(") ")
        #根据命令对消息做不同的处理。
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
        #基于消息生成文本数据。
        text = message + "\n"
        #将文本数据转换为二进制数据。
        binary = text.encode()
        #将二进制数据写入异步流。
        writer.write(binary)
        if message == "quit":
            break
    writer.close()


async def main():
    #创建服务器，并让其自动启动。
    server = await asyncio.start_server(engine, host, port)
    #等待60秒。
    await asyncio.sleep(60)
    #关闭服务器。
    server.close()
    sys.exit(0)


if __name__ == '__main__':
    asyncio.run(main())
