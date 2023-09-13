

from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from shahmMusic import app


def start_pannel(_):
    app = Client("@SHAHM4")

# استخدم هذا الديكوريتور لتحديد الدوال التي تستجيب للرسائل الواردة
@app.on_message(filters.private)
async def handle_message(client, message):
    # تحقق مما إذا كان المستخدم مشتركًا بالفعل
    if not await client.get_chat_member(chat_id="-1001895799003", user_id=message.from_user.id):
        # إرسال رسالة للمستخدم يطلب فيها الاشتراك الإجباري
        await message.reply_text("مرحبًا! يجب عليك الاشتراك حتى تتمكن من استخدام البوت.")
        # إرسال لوحة المفاتيح الخاصة بالاشتراك
        await message.reply_markup(start_pannel(None))

# قم بتشغيل البوت
app.run()
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

