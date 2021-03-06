from __future__ import annotations

from collections.abc import AsyncIterator
from typing import TYPE_CHECKING

from pylav._logging import getLogger
from pylav.sql import tables
from pylav.sql.models import PlayerStateModel

if TYPE_CHECKING:
    from pylav.client import Client

LOGGER = getLogger("PyLav.PlayerStateDBManager")


class PlayerStateDBManager:
    def __init__(self, client: Client):
        self._client = client

    @property
    def client(self) -> Client:
        return self._client

    async def save_players(self, players: list[dict]):
        for player in players:
            p = PlayerStateModel(bot=self.client.bot.user.id, **player)
            await p.save()
            LOGGER.trace("Saved player %s", p)
        LOGGER.debug("Saved %s players", len(players))

    async def save_player(self, player: dict):
        await PlayerStateModel(bot=self.client.bot.user.id, **player).save()

    async def get_player(self, guild_id: int) -> PlayerStateModel | None:
        return await PlayerStateModel.get(bot_id=self._client.bot.user.id, guild_id=guild_id)

    async def get_all_players(self) -> AsyncIterator[PlayerStateModel]:
        for entry in await tables.PlayerStateRow.select().where(tables.PlayerStateRow.bot == self.client.bot.user.id):  # type: ignore
            yield PlayerStateModel(**entry)

    async def delete_player(self, guild_id: int):
        await tables.PlayerStateRow.delete().where(
            (tables.PlayerStateRow.bot == self.client.bot.user.id) & (tables.PlayerStateRow.id == guild_id)
        )
