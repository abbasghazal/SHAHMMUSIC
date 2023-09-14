

from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from shahmMusic import app


def start_pannel(_):
    
    buttons = [
        [
            InlineKeyboardButton(
                text="‹ : الاوامر : ›",
                url=f"https://t.me/{app.username}?start=help",
            ),
            InlineKeyboardButton(text=_[""], callback_data="settings_helper"),
        ],
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(text="‹ : قناة الشروحات : ›", url=f"{SUPPORT_CHANNEL}"),
                InlineKeyboardButton(text="‹ : سورس شهم : ›", url=f"{SUPPORT_GROUP}"),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [InlineKeyboardButton(text="‹ : قناة الشروحات : ›", url=f"{SUPPORT_CHANNEL}")]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [InlineKeyboardButton(text="‹ : سورس شهم : ›", url=f"{SUPPORT_GROUP}")]
            )
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [InlineKeyboardButton(text="‹ : الاوامر : ›", callback_data="settings_back_helper")]
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(text="‹ : قناة الشروحات : ›", url=f"{SUPPORT_CHANNEL}"),
                InlineKeyboardButton(text="‹ : سورس شهم : ›", url=f"{SUPPORT_GROUP}"),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [InlineKeyboardButton(text="‹ : قناة الشروحات : ›", url=f"{SUPPORT_CHANNEL}")]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [InlineKeyboardButton(text="‹ : سورس شهم : ›", url=f"{SUPPORT_GROUP}")]
            )
    buttons.append(
        [
            InlineKeyboardButton(
                text="‹ : اضف البوت الى مجموعتك : ›",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ]
    )
    if GITHUB_REPO and OWNER:
        buttons.append(
            [
                InlineKeyboardButton(text="‹ : المطور : ›", user_id=OWNER),
                InlineKeyboardButton(text="‹ : لتنصيب بوت : ›", url=f"{GITHUB_REPO}"),
            ]
        )
    else:
        if GITHUB_REPO:
            buttons.append(
                [
                    InlineKeyboardButton(text="", url=f"{GITHUB_REPO}"),
                ]
            )
        if OWNER:
            buttons.append(
                [
                    InlineKeyboardButton(text="‹ : المطور : ›", user_id=OWNER),
                ]
            )
    buttons.append([InlineKeyboardButton(text="", callback_data="https://t.me/SAHAM4")])
    return buttons
