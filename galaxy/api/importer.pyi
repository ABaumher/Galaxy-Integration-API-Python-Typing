from logging import Logger

from .jsonrpc import ApplicationError
from ..task_manager import TaskManager

from typing import Awaitable, Callable, Generic, List, TypeVar

logger: Logger

IdentifierType = TypeVar('IdentifierType')
ContextType = TypeVar('ContextType')
GetType = TypeVar('GetType')

class Importer(Generic[IdentifierType, ContextType, GetType]):
    def __init__(self, task_manger : TaskManager, name: str, get: Callable[[IdentifierType, ContextType], Awaitable[List[GetType]]], prepare_context: Callable[[List[IdentifierType], Awaitable[ContextType]]], notification_success: Callable[[IdentifierType, GetType], None], notification_failure: Callable[[IdentifierType, ApplicationError], None], notification_finished: Callable[[], None], complete: Callable[[], None]) -> None: ...
    async def start(self, ids: List[IdentifierType]) -> None: ...

class CollectionImporter(Importer):
    def __init__(self, notification_partially_finished: Callable[[str], None], task_manger : TaskManager, name: str, get: Callable[[IdentifierType, ContextType], Awaitable[List[GetType]]], prepare_context: Callable[[List[IdentifierType], Awaitable[ContextType]]], notification_success: Callable[[IdentifierType, GetType], None], notification_failure: Callable[[IdentifierType, ApplicationError], None], notification_finished: Callable[[], None], complete: Callable[[], None]) -> None: ...

class SynchroneousImporter(Importer): ...
