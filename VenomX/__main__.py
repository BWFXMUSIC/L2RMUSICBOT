import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from PROFESSOR-SOURABH import LOGGER, app, userbot
from PROFESSOR-SOURABH.core.call import SOURABH
from PROFESSOR-SOURABH.misc import sudo
from PROFESSOR-SOURABH.plugins import ALL_MODULES
from PROFESSOR-SOURABH.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("PROFESSOR-SOURABH.plugins" + all_module)
    LOGGER("PROFESSOR-SOURABH.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await SOURABH.start()
    try:
        await SOURABH.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("PROFESSOR-SOURABH").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await SOURABH.decorators()
    LOGGER("PROFESSOR-SOURABH").info("ᴠᴇɴᴏᴍxᴍᴜsɪᴄ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ɴᴏᴡ ᴇɴᴊᴏʏ")

    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("PROFESSOR-SOURABH").info("Stopping PROFESSOR-SOURABH Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
