from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, SUPPORT_GROUP
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import sudo_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>๐๐๐ฒ ๐ {message.from_user.first_name}

๊ชษษญษญรธ, I ษษฑ ษษณ ษษโฑฑษษณฦษษ ฦคrษษฑษฉสษฑ โฑฎสsษฉฦ ฦคษญษฦดษr ฦรธส ฦrษษสษษ ฦฦด [SNEHU & ABHI ](t.me/SNEHABHI_SERVER). I ฦษษณ ฦคษญษฦด โฑฎสsษฉฦ ษฉษณ Yรธสr ฦฌษษญษสrษษฑ ฦษฆษษณษณษษญ รธr ฦrรธuฦฅ Vรธษฉฦษ ฦษฆษส ....

๐๐จ๐ฌ๐ญ๐๐ ๐๐ง ๐๐๐, ๐๐จ ๐ง๐จ ๐ฅ๐๐ 

๐ฅด๐๐๐๐ ๐๐๐ฅ๐ฉ!
๐๐ฌ๐ ๐๐ฎ๐ญ๐ญ๐จ๐ง๐ฌ ๐๐๐ฅ๐จ๐ฐ ๐๐จ ๐๐ง๐จ๐ฐ ๐๐จ๐ซ๐ ๐๐๐จ๐ฎ๐ญ ๐๐ ๐๐ง๐ ๐๐ฒ ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ๐
:-) ๐๐ผ๐ฟ ๐ ๐ผ๐ฟ๐ฒ ๐๐ป๐ณ๐ผ, ๐ฆ๐ฒ๐ป๐ฑ /help
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "๐ซ ๐ผ๐ฐ๐๐๐ธ ๐ถ๐๐พ๐๐ฟ ๐", url=f"https://t.me/LIVE_LIFE_LIKE")
                ],
                [
                    InlineKeyboardButton(
                         "๐ซ๐พ๐๐ฝ๐ด๐ ๐๐๐ด๐ด๐ฝโจ", url=f"https://t.me/ABHI_IS_MINE"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ซ๐๐๐ฟ๐ฟ๐พ๐๐ โจ", url=f"https://t.me/SNEHABHI_SERVER"
                    ),
                    InlineKeyboardButton(
                        "๐ซ ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ปโจ", url=f"https://t.me/SNEHABHI_UPDATES"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ซ๐พ๐๐ฝ๐ด๐ ๐บ๐ธ๐ฝ๐ถโจ", url=f"https://t.me/SNEHU_IS_MINE"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f""" ูญ๐ซ ๐๐ฝ๐ด๐ท๐ฐ๐ฑ๐ท๐ธ ๐ผ๐๐๐ธ๐ฒ๐โจูญ ๐๐จ๐ญ ๐๐ง๐ฅ๐ข๐ง๐ โ\n<b>๐๐๐ฉ๐ญ๐ข๐ฆ๐โ:</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ซ๐๐๐ฟ๐ฟ๐พ๐๐ โจ", url=f"https://t.me/IncognitoOff"
                    ),
                    InlineKeyboardButton(
                        "๐ซ ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ปโจ", url=f"https://t.me/IncognitoNetwork"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>๐๐ป **๐๐๐ฒ๐** {message.from_user.mention()}</b>

๐๐๐๐ ๐๐๐ฅ๐ฉ? 
๐๐ฌ๐ ๐๐ฎ๐ญ๐ญ๐จ๐ง๐ฌ ๐๐๐ฅ๐จ๐ฐ ๐๐จ ๐๐ง๐จ๐ฐ ๐๐จ๐ซ๐ ๐๐๐จ๐ฎ๐ญ ๐๐
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="๐๐จ๐ฐ ๐๐จ ๐๐ฌ๐?๐", callback_data=f"cbguide"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>๐๐ป **๐๐๐ฒ๐** {message.from_user.mention()}</b>

๐๐๐๐ ๐๐๐ฅ๐ฉ? 
๐๐ฌ๐ ๐๐ฎ๐ญ๐ญ๐จ๐ง๐ฌ ๐๐๐ฅ๐จ๐ฐ ๐๐จ ๐๐ง๐จ๐ฐ ๐๐จ๐ซ๐ ๐๐๐จ๐ฎ๐ญ ๐๐
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐๐จ๐ฐ ๐๐จ ๐๐ฌ๐?๐", callback_data="cbguide"
                    ),
                    InlineKeyboardButton(
                        "๐ซ ๐ผ๐ฐ๐๐๐ธ ๐ถ๐๐พ๐๐ฟ ๐", url=f"https://t.me/SNEHABHI_SERVER"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ซSU๐ฟ๐ฟ๐พ๐๐ โจ", url=f"https://t.me/SNEHABHI_SERVER"
                    ),
                    InlineKeyboardButton(
                        "๐ซ ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ปโจ", url=f"https://t.me/SNEHABHI_UPDATES"
                    )
                ],
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("แญIแGIแG....")
    delta_ping = time() - start
    await m_reply.edit_text(
        " `๐๐จ๐ง๐ !!`\n"
        f" `{delta_ping * 1000:.3f} แดนหข`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "๐๐จ๐ญ ๐๐ญ๐๐ญ๐ฎ๐ฌ๐:\n"
        f"โข **๐๐๐๐๐๐:** `{uptime}`\n"
        f"โข **๐๐๐๐๐ ๐๐๐๐:** `{START_TIME_ISO}`"
    )
