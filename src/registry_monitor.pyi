from _typeshed import Incomplete
from ctypes.wintypes import LPVOID

LPSECURITY_ATTRIBUTES = LPVOID
RegOpenKeyEx: Incomplete
RegCloseKey: Incomplete
RegNotifyChangeKeyValue: Incomplete
CloseHandle: Incomplete
CreateEvent: Incomplete
WaitForSingleObject: Incomplete
ERROR_SUCCESS: int
KEY_READ: int
KEY_QUERY_VALUE: int
REG_NOTIFY_CHANGE_NAME: int
REG_NOTIFY_CHANGE_LAST_SET: int
WAIT_OBJECT_0: int
WAIT_TIMEOUT: int

class RegistryMonitor:
    def __init__(self, root, subkey) -> None: ...
    def close(self) -> None: ...
    def is_updated(self): ...
