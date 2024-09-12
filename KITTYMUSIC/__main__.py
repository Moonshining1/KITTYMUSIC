#
# Copyright (C) 2024 by Moonshining1@Github, < https://github.com/Moonshining1 >.
#
# This file is part of < https://github.com/Moonshining1/KITTYMUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/Moonshining1/KITTYMUSIC/blob/master/LICENSE >
#
# All rights reserved.
import asyncio
import importlib

from pyrogram import idle

import config
from config import BANNED_USERS
from KITTYMUSIC import HELPABLE, LOGGER, app, userbot
from KITTYMUSIC.core.call import KITTY
from KITTYMUSIC.plugins import ALL_MODULES
from KITTYMUSIC.utils.database import get_banned_users, get_gbanned


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("KITTYMUSIC").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if not config.SPOTIFY_CLIENT_ID and not config.SPOTIFY_CLIENT_SECRET:
        LOGGER("KITTYMUSIC").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception:
        pass

    await app.start()

    for all_module in ALL_MODULES:
        imported_module = importlib.import_module(all_module)

        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELPABLE[imported_module.__MODULE__.lower()] = imported_module
    LOGGER("KITTYMUSIC.plugins").info("Successfully Imported All Modules ")

    await userbot.start()
    await KITTY.start()
    await KITTY.decorators()
    LOGGER("KITTYMUSIC").info("KITTYMUSIC STARTED SUCCESSFULLY 🕊️")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop_policy().get_event_loop().run_until_complete(init())
    LOGGER("KITTYMUSIC").info("Stopping KITTYMUSIC! GoodBye")
