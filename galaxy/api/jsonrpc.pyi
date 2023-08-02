from asyncio import StreamReader, StreamWriter
from inspect import Signature
from json import JSONEncoder
from logging import Logger
from typing import Any, Callable, Dict, Iterable, List, NamedTuple, Optional, Union
from collections.abc import Mapping

logger: Logger

class JsonRpcError(Exception):
    code: int
    message: str
    data: Optional[Mapping]
    def __init__(self, code: int, message: Any, data: Optional[Mapping]) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def json(self) -> Dict[str, Any]: ...

class ParseError(JsonRpcError):
    def __init__(self, message: str, data: Mapping) -> None: ...

class InvalidRequest(JsonRpcError):
    def __init__(self, message: str, data: Mapping) -> None: ...

class MethodNotFound(JsonRpcError):
    def __init__(self, message: str, data: Mapping) -> None: ...

class InvalidParams(JsonRpcError):
    def __init__(self, message: str, data: Mapping) -> None: ...

class Timeout(JsonRpcError):
    def __init__(self, message: str, data: Mapping) -> None: ...

class Aborted(JsonRpcError):
    def __init__(self, message: str, data: Mapping) -> None: ...

class ApplicationError(JsonRpcError):
    def __init__(self, code: int, message: str, data: Mapping) -> None: ...

class UnknownError(ApplicationError):
    def __init__(self, message: str, data: Mapping) -> None: ...

class Request(NamedTuple):
    method: str
    params: Optional[List[Any]]
    id: int

class Response(NamedTuple):
    id: int
    result: Any
    error: Optional[Exception]

class Method(NamedTuple):
    callback: Callable
    signature: Signature
    immediate: bool
    sensitive_params: bool

def anonymise_sensitive_params(params: Dict[str, Any], sensitive_params: Union[bool, Iterable]): ...

class Connection:
    def __init__(self, reader: StreamReader, writer: StreamWriter, encoder: JSONEncoder) -> None: ...
    def register_method(self, name: str, callback: Callable, immediate: bool, sensitive_params: bool = ...) -> None: ...
    def register_notification(self, name: str, callback: Callable, immediate: bool, sensitive_params: bool = ...) -> None: ...
    async def send_request(self, method: str, params : Dict[str, Any], sensitive_params: Union[bool, Iterable[str]]): ...
    def send_notification(self, method: str, params, sensitive_params: Union[bool, Iterable[str]]) -> None: ...
    async def run(self) -> None: ...
    def close(self) -> None: ...
    async def wait_closed(self) -> None: ...
