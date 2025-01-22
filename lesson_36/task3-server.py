import asyncio


async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"New connection from {addr}")

    while True:
        try:
            # Read message from client
            data = await reader.read(100)
            message = data.decode().strip()

            if not message:
                print(f"Connection closed by {addr}")
                break

            print(f"Received '{message}' from {addr}")

            # Echo the message back to the client
            writer.write(data)
            await writer.drain()

        except asyncio.CancelledError:
            break

    writer.close()
    await writer.wait_closed()
    print(f"Connection with {addr} terminated.")


async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f"Server started on {addr}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer stopped.")
