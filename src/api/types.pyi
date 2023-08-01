from galaxy.api.consts import LicenseType as LicenseType, LocalGameState as LocalGameState, PresenceState as PresenceState, SubscriptionDiscovery as SubscriptionDiscovery
from typing import Dict, List, Optional

class Authentication:
    user_id: str
    user_name: str
    def __init__(self, user_id, user_name) -> None: ...

class Cookie:
    name: str
    value: str
    domain: Optional[str]
    path: Optional[str]
    def __init__(self, name, value, domain, path) -> None: ...

class NextStep:
    next_step: str
    auth_params: Dict[str, str]
    cookies: Optional[List[Cookie]]
    js: Optional[Dict[str, List[str]]]
    def __init__(self, next_step, auth_params, cookies, js) -> None: ...

class LicenseInfo:
    license_type: LicenseType
    owner: Optional[str]
    def __init__(self, license_type, owner) -> None: ...

class Dlc:
    dlc_id: str
    dlc_title: str
    license_info: LicenseInfo
    def __init__(self, dlc_id, dlc_title, license_info) -> None: ...

class Game:
    game_id: str
    game_title: str
    dlcs: Optional[List[Dlc]]
    license_info: LicenseInfo
    def __init__(self, game_id, game_title, dlcs, license_info) -> None: ...

class Achievement:
    unlock_time: int
    achievement_id: Optional[str]
    achievement_name: Optional[str]
    def __post_init__(self) -> None: ...
    def __init__(self, unlock_time, achievement_id, achievement_name) -> None: ...

class LocalGame:
    game_id: str
    local_game_state: LocalGameState
    def __init__(self, game_id, local_game_state) -> None: ...

class FriendInfo:
    user_id: str
    user_name: str
    def __init__(self, user_id, user_name) -> None: ...

class UserInfo:
    user_id: str
    user_name: str
    avatar_url: Optional[str]
    profile_url: Optional[str]
    def __init__(self, user_id, user_name, avatar_url, profile_url) -> None: ...

class GameTime:
    game_id: str
    time_played: Optional[int]
    last_played_time: Optional[int]
    def __init__(self, game_id, time_played, last_played_time) -> None: ...

class GameLibrarySettings:
    game_id: str
    tags: Optional[List[str]]
    hidden: Optional[bool]
    def __init__(self, game_id, tags, hidden) -> None: ...

class UserPresence:
    presence_state: PresenceState
    game_id: Optional[str]
    game_title: Optional[str]
    in_game_status: Optional[str]
    full_status: Optional[str]
    def __init__(self, presence_state, game_id, game_title, in_game_status, full_status) -> None: ...

class Subscription:
    subscription_name: str
    owned: Optional[bool]
    end_time: Optional[int]
    subscription_discovery: SubscriptionDiscovery
    def __post_init__(self) -> None: ...
    def __init__(self, subscription_name, owned, end_time, subscription_discovery) -> None: ...

class SubscriptionGame:
    game_title: str
    game_id: str
    start_time: Optional[int]
    end_time: Optional[int]
    def __init__(self, game_title, game_id, start_time, end_time) -> None: ...
