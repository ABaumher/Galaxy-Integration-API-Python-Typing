import json
from _typeshed import Incomplete
from logging import Logger
from types import TracebackType
from galaxy.api.consts import Feature as Feature, OSCompatibility as OSCompatibility
from galaxy.api.importer import CollectionImporter as CollectionImporter, Importer as Importer, SynchroneousImporter as SynchroneousImporter
from galaxy.api.jsonrpc import ApplicationError as ApplicationError, Connection as Connection
from galaxy.api.types import Achievement as Achievement, Authentication as Authentication, Game as Game, GameLibrarySettings as GameLibrarySettings, GameTime as GameTime, LocalGame as LocalGame, NextStep as NextStep, Subscription as Subscription, SubscriptionGame as SubscriptionGame, UserInfo as UserInfo, UserPresence as UserPresence
from galaxy.task_manager import TaskManager as TaskManager
from typing import Any, AsyncGenerator, Coroutine, Dict, List, Optional, Type, TypeVar, Union

logger: Logger

class JSONEncoder(json.JSONEncoder):
    def default(self, o: Any): ...

class Plugin:
    def __init__(self, platform, version, reader, writer, handshake_token) -> None: ...
    async def __aenter__(self): ...
    async def __aexit__(self, exc_type: Optional[Type], exc: Optional[BaseException], tb: Optional[TracebackType]) -> None: ...
    @property
    def features(self) -> List[Feature]: ...
    @property
    def persistent_cache(self) -> Dict[str, str]: ...
    async def run(self) -> None: ...
    def close(self) -> None: ...
    async def wait_closed(self) -> None: ...
    def create_task(self, coro: Coroutine[None, None, Any], description: str): ...
    def store_credentials(self, credentials: Dict[str, Any]) -> None: ...
    def add_game(self, game: Game) -> None: ...
    def remove_game(self, game_id: str) -> None: ...
    def update_game(self, game: Game) -> None: ...
    def unlock_achievement(self, game_id: str, achievement: Achievement) -> None: ...
    def update_local_game_status(self, local_game: LocalGame) -> None: ...
    def add_friend(self, user: UserInfo) -> None: ...
    def remove_friend(self, user_id: str) -> None: ...
    def update_friend_info(self, user: UserInfo) -> None: ...
    def update_game_time(self, game_time: GameTime) -> None: ...
    def update_user_presence(self, user_id: str, user_presence: UserPresence) -> None: ...
    def lost_authentication(self) -> None: ...
    def push_cache(self) -> None: ...
    async def refresh_credentials(self, params: Dict[str, Any], sensitive_params: Union[bool, List[str]]) -> Dict[str, Any]: ...
    def handshake_complete(self) -> None: ...
    def tick(self) -> None: ...
    async def shutdown(self) -> None: ...
    async def authenticate(self, stored_credentials: Optional[Dict[str, Any]]) -> Union[NextStep, Authentication]: ...
    async def pass_login_credentials(self, step: str, credentials: Dict[str, str], cookies: List[Dict[str, str]]) -> Union[NextStep, Authentication]: ...
    async def get_owned_games(self) -> List[Game]: ...
    AchievementContext = TypeVar["AchievementContext"]
    async def prepare_achievements_context(self, game_ids: List[str]) -> AchievementContext: ...
    async def get_unlocked_achievements(self, game_id: str, context: AchievementContext) -> List[Achievement]: ...
    def achievements_import_complete(self) -> None: ...
    async def get_local_games(self) -> List[LocalGame]: ...
    async def launch_game(self, game_id: str) -> None: ...
    async def install_game(self, game_id: str) -> None: ...
    async def uninstall_game(self, game_id: str) -> None: ...
    async def shutdown_platform_client(self) -> None: ...
    async def launch_platform_client(self) -> None: ...
    async def get_friends(self) -> List[UserInfo]: ...
    GameTimeContext = TypeVar["GameTimeContext"]
    async def prepare_game_times_context(self, game_ids: List[str]) -> GameTimeContext: ...
    async def get_game_time(self, game_id: str, context: GameTimeContext) -> GameTime: ...
    def game_times_import_complete(self) -> None: ...
    LibrarySettingContext = TypeVar["LibrarySettingContext"]
    async def prepare_game_library_settings_context(self, game_ids: List[str]) -> LibrarySettingContext: ...
    async def get_game_library_settings(self, game_id: str, context: LibrarySettingContext) -> GameLibrarySettings: ...
    def game_library_settings_import_complete(self) -> None: ...
    OSCompatibilityContext = TypeVar["OSCompatibilityContext"]
    async def prepare_os_compatibility_context(self, game_ids: List[str]) -> OSCompatibilityContext: ...
    async def get_os_compatibility(self, game_id: str, context: OSCompatibilityContext) -> Optional[OSCompatibility]: ...
    def os_compatibility_import_complete(self) -> None: ...
    UserPresenceContext = TypeVar["UserPresenceContext"]
    async def prepare_user_presence_context(self, user_id_list: List[str]) -> UserPresenceContext: ...
    async def get_user_presence(self, user_id: str, context: UserPresenceContext) -> UserPresence: ...
    def user_presence_import_complete(self) -> None: ...
    LocalSizeContext = TypeVar["LocalSizeContext"]
    async def prepare_local_size_context(self, game_ids: List[str]) -> LocalSizeContext: ...
    async def get_local_size(self, game_id: str, context: LocalSizeContext) -> Optional[int]: ...
    def local_size_import_complete(self) -> None: ...
    async def get_subscriptions(self) -> List[Subscription]: ...
    SubscriptionGameContext = TypeVar["SubscriptionGameContext"]
    async def prepare_subscription_games_context(self, subscription_names: List[str]) -> SubscriptionGameContext: ...
    async def get_subscription_games(self, subscription_name: str, context: SubscriptionGameContext) -> AsyncGenerator[List[SubscriptionGame], None]: ...
    def subscription_games_import_complete(self) -> None: ...

def create_and_run_plugin(plugin_class: Type, argv: List[str]) -> None: ...
