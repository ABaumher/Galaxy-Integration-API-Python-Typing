from asyncio import StreamReader

class StreamLineReader:
    def __init__(self, reader: StreamReader) -> None: ...
    async def readline(self) -> bytes: ...