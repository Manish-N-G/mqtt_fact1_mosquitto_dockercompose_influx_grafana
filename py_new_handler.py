'''
import asyncio
import websockets

async def handle_connection(websocket, path):
    while True:
        message = await websocket.recv()
        print(f"Received: {message}")
        # You can add additional processing here

async def main():
    server = await websockets.serve(handle_connection, "localhost", 8765)
    await server.wait_closed()

# Run the WebSocket server
asyncio.get_event_loop().run_until_complete(main())
'''
import asyncio
import websockets

async def handle_connection(websocket, path):
    while True:
        message = await websocket.recv()
        print(f"Received message: {message}")
        # You can add additional processing here

async def main():
    server = await websockets.serve(handle_connection, "localhost", 8765)
    await server.wait_closed()

# Run the WebSocket server
asyncio.get_event_loop().run_until_complete(main())