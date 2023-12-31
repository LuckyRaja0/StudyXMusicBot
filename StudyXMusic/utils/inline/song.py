#
# Copyright (C) 2021-2022 by Luckyraja0@Github, < https://github.com/Luckyraja0 >.
#
# This file is part of < https://github.com/LuckyRaja0/StudyXMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/LuckyRaja0/StudyXMusicBot/blob/nobi/LICENSE >
#
# All rights reserved.

from pyrogram.types import InlineKeyboardButton


def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons
