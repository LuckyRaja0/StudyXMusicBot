#
# Copyright (C) 2021-2022 by Luckyraja0@Github, < https://github.com/Luckyraja0 >.
#
# This file is part of < https://github.com/LuckyRaja0/StudyXMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/LuckyRaja0/StudyXMusicBot/blob/nobi/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from StudyXMusic import app
from StudyXMusic.core.call import StudyX
from StudyXMusic.utils.database import is_muted, mute_on
from StudyXMusic.utils.decorators import AdminRightsCheck

# Commands
MUTE_COMMAND = get_command("MUTE_COMMAND")


@app.on_message(
    filters.command(MUTE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def mute_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text(_["general_2"])
    if await is_muted(chat_id):
        return await message.reply_text(_["admin_5"])
    await mute_on(chat_id)
    await StudyX.mute_stream(chat_id)
    await message.reply_text(
        _["admin_6"].format(message.from_user.mention)
    )
