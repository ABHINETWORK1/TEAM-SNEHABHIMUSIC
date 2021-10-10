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
        f"""<b>𝐇𝐞𝐲 👋 {message.from_user.first_name}

Ɦɘɭɭø, I ɑɱ ɑɳ Ʌɗⱱɑɳƈɘɗ Ƥrɘɱɩʋɱ Ɱʉsɩƈ Ƥɭɑƴɘr Ɓøʈ Ƈrɘɑʈɘɗ Ɓƴ [SNEHU & ABHI ](t.me/SNEHABHI_SERVER). I Ƈɑɳ Ƥɭɑƴ Ɱʉsɩƈ ɩɳ Yøʋr Ƭɘɭɘʛrɑɱ Ƈɦɑɳɳɘɭ ør Ɠrøuƥ Vøɩƈɘ Ƈɦɑʈ ....

𝐇𝐨𝐬𝐭𝐞𝐝 𝐎𝐧 𝐕𝐏𝐒, 𝐒𝐨 𝐧𝐨 𝐥𝐚𝐠

🥴𝐍𝐞𝐞𝐝 𝐇𝐞𝐥𝐩!
𝐔𝐬𝐞 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐁𝐞𝐥𝐨𝐰 𝐓𝐨 𝐊𝐧𝐨𝐰 𝐌𝐨𝐫𝐞 𝐀𝐛𝐨𝐮𝐭 𝐌𝐞 𝐚𝐧𝐝 𝐌𝐲 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬😁
:-) 𝗙𝗼𝗿 𝗠𝗼𝗿𝗲 𝗜𝗻𝗳𝗼, 𝗦𝗲𝗻𝗱 /help
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "💫 𝙼𝙰𝚂𝚃𝙸 𝙶𝚁𝙾𝚄𝙿 👈", url=f"https://t.me/LIVE_LIFE_LIKE")
                ],
                [
                    InlineKeyboardButton(
                         "💫𝙾𝚆𝙽𝙴𝚁 𝚀𝚄𝙴𝙴𝙽✨", url=f"https://t.me/ABHI_IS_MINE"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💫𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ✨", url=f"https://t.me/SNEHABHI_SERVER"
                    ),
                    InlineKeyboardButton(
                        "💫 𝙲𝙷𝙰𝙽𝙽𝙴𝙻✨", url=f"https://t.me/SNEHABHI_UPDATES"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💫𝙾𝚆𝙽𝙴𝚁 𝙺𝙸𝙽𝙶✨", url=f"https://t.me/SNEHU_IS_MINE"
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
        f""" ٭💫 𝚂𝙽𝙴𝙷𝙰𝙱𝙷𝙸 𝙼𝚄𝚂𝙸𝙲𝚂✨٭ 𝐁𝐨𝐭 𝐎𝐧𝐥𝐢𝐧𝐞 ✅\n<b>😇𝐔𝐩𝐭𝐢𝐦𝐞✌:</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💫𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ✨", url=f"https://t.me/IncognitoOff"
                    ),
                    InlineKeyboardButton(
                        "💫 𝙲𝙷𝙰𝙽𝙽𝙴𝙻✨", url=f"https://t.me/IncognitoNetwork"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 **𝐇𝐞𝐲𝐚** {message.from_user.mention()}</b>

𝐍𝐞𝐞𝐝 𝐇𝐞𝐥𝐩? 
𝐔𝐬𝐞 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐁𝐞𝐥𝐨𝐰 𝐓𝐨 𝐊𝐧𝐨𝐰 𝐌𝐨𝐫𝐞 𝐀𝐛𝐨𝐮𝐭 𝐌𝐞
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="𝐇𝐨𝐰 𝐓𝐨 𝐔𝐬𝐞?💎", callback_data=f"cbguide"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 **𝐇𝐞𝐲𝐚** {message.from_user.mention()}</b>

𝐍𝐞𝐞𝐝 𝐇𝐞𝐥𝐩? 
𝐔𝐬𝐞 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 𝐁𝐞𝐥𝐨𝐰 𝐓𝐨 𝐊𝐧𝐨𝐰 𝐌𝐨𝐫𝐞 𝐀𝐛𝐨𝐮𝐭 𝐌𝐞
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐇𝐨𝐰 𝐓𝐨 𝐔𝐬𝐞?💎", callback_data="cbguide"
                    ),
                    InlineKeyboardButton(
                        "💫 𝙼𝙰𝚂𝚃𝙸 𝙶𝚁𝙾𝚄𝙿 👈", url=f"https://t.me/SNEHABHI_SERVER"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💫SU𝙿𝙿𝙾𝚁𝚃 ✨", url=f"https://t.me/SNEHABHI_SERVER"
                    ),
                    InlineKeyboardButton(
                        "💫 𝙲𝙷𝙰𝙽𝙽𝙴𝙻✨", url=f"https://t.me/SNEHABHI_UPDATES"
                    )
                ],
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᑭIᑎGIᑎG....")
    delta_ping = time() - start
    await m_reply.edit_text(
        " `𝐏𝐨𝐧𝐠!!`\n"
        f" `{delta_ping * 1000:.3f} ᴹˢ`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐮𝐬💚:\n"
        f"• **𝚄𝚙𝚝𝚒𝚖𝚎:** `{uptime}`\n"
        f"• **𝚂𝚝𝚊𝚛𝚝 𝚃𝚒𝚖𝚎:** `{START_TIME_ISO}`"
    )
