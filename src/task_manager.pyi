from _typeshed import Incomplete

logger: Incomplete

class TaskManager:
    def __init__(self, name) -> None: ...
    def create_task(self, coro, description, handle_exceptions: bool = ...): ...
    def cancel(self) -> None: ...
    async def wait(self) -> None: ...