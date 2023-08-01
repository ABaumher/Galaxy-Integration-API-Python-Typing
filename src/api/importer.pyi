from _typeshed import Incomplete
from galaxy.api.errors import ImportInProgress as ImportInProgress, UnknownError as UnknownError
from galaxy.api.jsonrpc import ApplicationError as ApplicationError

logger: Incomplete

class Importer:
    def __init__(self, task_manger, name, get, prepare_context, notification_success, notification_failure, notification_finished, complete) -> None: ...
    async def start(self, ids) -> None: ...

class CollectionImporter(Importer):
    def __init__(self, notification_partially_finished, *args) -> None: ...

class SynchroneousImporter(Importer): ...
