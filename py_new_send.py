'''
import asyncio
import websockets

async def send_messages():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        for i in range(10):
            message = f"Hello {i + 1}"
            print(f"Sending: {message}")
            await websocket.send(message)
            await asyncio.sleep(1)

# Run the sender loop
asyncio.get_event_loop().run_until_complete(send_messages())
'''
import asyncio
import websockets

async def send_messages():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        for i in range(10):
            message = f"Hello {i + 1}"
            print(f"Sending: {message}")  # this is for just the terminal
            await websocket.send(message)
            await asyncio.sleep(1)

# Run the sender loop
asyncio.get_event_loop().run_until_complete(send_messages())