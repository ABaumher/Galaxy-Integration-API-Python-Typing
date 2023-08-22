from .consts import LicenseType, LocalGameState, PresenceState, SubscriptionDiscovery
from typing import Dict, List, Optional, Union

class Authentication:
    user_id: str
    user_name: str
    def __init__(self, user_id: str, user_name: str) -> None: ...

class Cookie:
    name: str
    value: str
    domain: Optional[str]
    path: Optional[str]
    def __init__(self, name: str, value:str , domain: Optional[str] = ..., path: Optional[str] = ...) -> None: ...

class NextStep:
    next_step: str
    auth_params: Dict[str, Union[int, str]]  # in the plugin this is typed as Dict[str, str] but some of the expected keys map to int per their documentation. 
    cookies: Optional[List[Cookie]]
    js: Optional[Dict[str, List[str]]]
    def __init__(self, next_step: str, auth_params: Dict[str, Union[int, str]], cookies: Optional[List[Cookie]] = ..., js: Optional[Dict[str, List[str]]] = ...) -> None: ...

class LicenseInfo:
    license_type: LicenseType
    owner: Optional[str]
    def __init__(self, license_type: LicenseType, owner: Optional[str] = ...) -> None: ...

class Dlc:
    dlc_id: str
    dlc_title: str
    license_info: LicenseInfo
    def __init__(self, dlc_id: str, dlc_title: str, license_info: LicenseInfo) -> None: ...

class Game:
    game_id: str
    game_title: str
    dlcs: Optional[List[Dlc]]
    license_info: LicenseInfo
    def __init__(self, game_id: str, game_title: str, dlcs: Optional[List[Dlc]], license_info: LicenseInfo) -> None: ...

class Achievement:
    unlock_time: int
    achievement_id: Optional[str]
    achievement_name: Optional[str]
    def __post_init__(self) -> None: ...
    def __init__(self, unlock_time: int, achievement_id: Optional[str] = ..., achievement_name: Optional[str] = ...) -> None: ...

class LocalGame:
    game_id: str
    local_game_state: LocalGameState
    def __init__(self, game_id: str, local_game_state: LocalGameState) -> None: ...

class FriendInfo:
    user_id: str
    user_name: str
    def __init__(self, user_id: str, user_name: str) -> None: ...

class UserInfo:
    user_id: str
    user_name: str
    avatar_url: Optional[str]
    profile_url: Optional[str]
    def __init__(self, user_id: str, user_name: str, avatar_url: Optional[str] = ..., profile_url: Optional[str] = ...) -> None: ...

class GameTime:
    game_id: str
    time_played: Optional[int]
    last_played_time: Optional[int]
    def __init__(self, game_id: str, time_played: Optional[int], last_played_time: Optional[int]) -> None: ...

class GameLibrarySettings:
    game_id: str
    tags: Optional[List[str]]
    hidden: Optional[bool]
    def __init__(self, game_id: str, tags: Optional[List[str]], hidden: Optional[bool]) -> None: ...

class UserPresence:
    presence_state: PresenceState
    game_id: Optional[str]
    game_title: Optional[str]
    in_game_status: Optional[str]
    full_status: Optional[str]
    def __init__(self, presence_state: PresenceState, game_id: Optional[str] = ..., game_title: Optional[str] = ..., in_game_status: Optional[str] = ..., full_status: Optional[str] = ...) -> None: ...

class Subscription:
    subscription_name: str
    owned: Optional[bool]
    end_time: Optional[int]
    subscription_discovery: SubscriptionDiscovery
    def __post_init__(self) -> None: ...
    def __init__(self, subscription_name: str, owned: Optional[bool] = ..., end_time: Optional[int] = ..., subscription_discovery: SubscriptionDiscovery = ...) -> None: ...

class SubscriptionGame:
    game_title: str
    game_id: str
    start_time: Optional[int]
    end_time: Optional[int]
    def __init__(self, game_title: str, game_id: str, start_time: Optional[int] = ..., end_time: Optional[int] = ...) -> None: ...
