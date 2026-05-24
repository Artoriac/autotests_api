import asyncio

import websockets
from websockets import ServerConnection


async def echo(websocket: ServerConnection):
    async for message in websocket:
        for _ in range(1, 6):
            print(f"{_} Получено сообщение от пользователя:: {message}")
            response = f"Сервер получил сообщение: {message}"
            await websocket.send(response)

async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("Websocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()

asyncio.run(main())