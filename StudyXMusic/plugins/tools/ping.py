#
# Copyright (C) 2021-2022 by Luckyraja0@Github, < https://github.com/Luckyraja0 >.
#
# This file is part of < https://github.com/LuckyRaja0/StudyXMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/LuckyRaja0/StudyXMusicBot/blob/nobi/LICENSE >
#
# All rights reserved.

from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from strings import get_command
from StudyXMusic import app
from StudyXMusic.core.call import StudyX
from StudyXMusic.utils import bot_sys_stats
from StudyXMusic.utils.decorators.language import language

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(
    filters.command(PING_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await StudyX.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            MUSIC_BOT_NAME, resp, UP, DISK, CPU, RAM, pytgping
        )
    )