import asyncio
from aiohttp import web

async def index(request):
    return web.FileResponse('./index4.html')

async def read_number_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return str(e)

async def send_number(file_path, key, ws):
    last_sent_number = None
    while True:
        try:
            number = await read_number_from_file(file_path)
            if last_sent_number != number:
                await ws.send_json({key: number})
                last_sent_number = number
            await asyncio.sleep(1)  # Adjust the sleep time as needed
        except ConnectionResetError:
            print(f"Connection lost while sending data from {file_path}.")
            break  # Exit the loop if the connection is closed
        except asyncio.CancelledError:
            break  # Exit the loop if the coroutine is cancelled
        except Exception as e:
            print(f"Unexpected error: {e}")
            break  # Exit the loop on other exceptions

async def save_number_to_file(file_path, number):
    try:
        with open(file_path, 'w') as file:
            file.write(str(number))
    except Exception as e:
        print(f"Error writing to {file_path}: {e}")

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    task1 = asyncio.create_task(send_number('test.txt', 'number1', ws))
    task2 = asyncio.create_task(send_number('test1.txt', 'number2', ws))

    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT:
            data = msg.json()
            if 'sliderValue' in data:
                await save_number_to_file('test3.txt', data['sliderValue'])
        elif msg.type == web.WSMsgType.ERROR:
            print('WebSocket connection closed with exception %s' % ws.exception())

    task1.cancel()
    task2.cancel()
    await task1
    await task2
    print('WebSocket connection closed')
    return ws

app = web.Application()
app.router.add_get('/', index)
app.router.add_get('/echo', websocket_handler)

if __name__ == '__main__':
    web.run_app(app, port=5000)