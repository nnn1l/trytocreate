import asyncio


async def send_message(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    print(f"Sending: {message}")
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f"Received: {data.decode().strip()}")

    writer.close()
    await writer.wait_closed()


async def main():
    messages = [
        "Hello, Server!",
        "How are you?",
        "This is a test.",
        "Goodbye!",
    ]

    await asyncio.gather(*(send_message(msg) for msg in messages))


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nClient stopped.")
