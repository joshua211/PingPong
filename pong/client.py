import datetime
import os
import asyncio
import websockets

async def pong():
    # Die Server-Adresse wird aus der Umgebungsvariable geladen
    #server_address = os.getenv("PING_SERVER_ADDRESS", "ws://localhost:8765")
    server_address = "wss://echo.websocket.org"

    async with websockets.connect(server_address) as websocket:
        while True:
            # Empfang der Nachricht vom Server
            await websocket.send("Ping")
            message = await websocket.recv()
            print(f"Received: {message}" + str(datetime.datetime.now()))
            
            await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(pong())
    except Exception as e:
        print(e)
    
    #az container create --resource-group rg-bmg-hosting-test --name ping-server --image crbmgtestwesteurope.azurecr.io/ping-server:latest --dns-name-label prodot-ping-server --ports 8765
    
    #az container create --resource-group rg-bmg-hosting-test --name pong-client --image crbmgtestwesteurope.azurecr.io/pong-client:latest --environment-variables PING_SERVER_ADDRESS=ws://prodot-ping-server:8765