import asyncio
import websockets
import json

async def send_aac_message(uri, message):
    try:
        async with websockets.connect(uri) as websocket:
            print("✅ Connected to WebSocket server")
            await websocket.send(json.dumps(message))
            print("📤 Message sent successfully")
            response = await websocket.recv()
            print(f"📝 Server response: {response}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Edit this message for future tests
    test_message = {
        "text": "water yummy more",
        "user_id": "vedant",
        "metadata": json.dumps({"source": "web"})
    }
    # Convert metadata to JSON string if your server expects a string
    if isinstance(test_message.get("metadata"), dict):
        test_message["metadata"] = json.dumps(test_message["metadata"])
    
    asyncio.run(send_aac_message("ws://localhost:8765", test_message))