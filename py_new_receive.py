'''
import asyncio
import websockets

async def receive_messages():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        for i in range(10):
            message = await websocket.recv()
            print(f"Received: {message}")

        # Send acknowledgment after receiving 10 messages
        await websocket.send("Received 10 messages")

# Run the receiver loop
asyncio.get_event_loop().run_until_complete(receive_messages())
'''
import asyncio
import websockets

async def receive_messages():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        for i in range(10):
            message = await websocket.recv()
            print(f"Received: {message}")

        # Send acknowledgment after receiving 10 messages
        await websocket.send("Received 10 messages")

# Run the receiver loop
asyncio.get_event_loop().run_until_complete(receive_messages())