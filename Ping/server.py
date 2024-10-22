import asyncio
import datetime
import websockets

async def ping(websocket, path):
    while True:
        # Send a ping message to the client
        await websocket.send("Ping")
        # print ping and current date
        print(f"Sent: Ping" + str(datetime.datetime.now()))
        
        # Wait for the pong response
        response = await websocket.recv()
        print(f"Received: {response}" + str(datetime.datetime.now()))
        
        # Wait for 1 seconds before sending the next ping
        await asyncio.sleep(1)

async def main():
    async with websockets.serve(ping, "0.0.0.0", 8765):
        print("WebSocket server started on ws://0.0.0.0:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    print("WebSocket server started")
    asyncio.run(main())