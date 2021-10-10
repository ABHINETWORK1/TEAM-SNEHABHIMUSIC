# this module i created only for playing music using audio file, idk, because the audio player on play.py module not working
# so this is the alternative
# audio play function

from os import path

from pyrogram import Client
from pyrogram.types import Message, Voice

from services.callsmusic import callsmusic, queues

import services.converter
from services.downloaders import youtube

from config import BOT_NAME as bn, DURATION_LIMIT, UPDATES_CHANNEL, BG_IMAGE, SUPPORT_GROUP
from helpers.filters import command, other_filters
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(command("fplay") & other_filters)
@errors
async def stream(_, message: Message):

    lel = await message.reply("R𝚄𝙺𝙾 𝚉𝙰𝚁𝙰 𝚂𝙰𝙱𝙰𝚁 𝙺𝙰𝚁𝙾 ⭐ 𝚂𝙾𝙽𝙶 𝙳𝙷𝚄𝙽𝙳𝙷 𝚁𝙰𝙷𝙰 𝙷𝚄 ❤️😋...uploaded by @SNEHABHI_SERVER  ♩✌")
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="💫𝚂𝚄𝙿𝙿𝙾𝚁T✨",
                        url=f"https://t.me/SNEHABHI_SERVER"),
                    InlineKeyboardButton(
                        text="💫 𝙲𝙷𝙰𝙽𝙽𝙴𝙻✨",
                        url=f"https://t.me/ABHI_NETWORK1")
                ],[

                    InlineKeyboardButton(

                           text="💫 𝙼𝙰𝚂𝚃𝙸 𝙶𝚁𝙾𝚄𝙿 👈", url=f"https://t.me/LIVE_LIKE_LIFE")

            ],[       

                    InlineKeyboardButton(

                           text="💫𝙾𝚆𝙽𝙴𝚁 𝙺𝙸𝙽𝙶✨", url=f"https://t.me/SNEHU_IS_MINE")

            ],[           

                    InlineKeyboardButton(

                           text="💫𝙾𝚆𝙽𝙴𝚁 𝚀𝚄𝙴𝙴𝙽✨", url=f"HTTP://T.ME/ABHI_IS_MINE")

                ]
            ]
        )

    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"❌ Videos longer than {DURATION_LIMIT} minute(s) aren't allowed to play!"
            )

        file_name = get_file_name(audio)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await lel.edit_text("🎶 Beta jao song ka nam acche se dekh kar ao.. aisa koi song nahi ha merepass 👀...uploaded by @SNEHABHI_SERVER ✨")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
        photo=f"{BG_IMAGE}",
        reply_markup=keyboard,
        caption=f"#⃣ 𝐘𝐨𝐮𝐫 𝐫𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝 𝐬𝐨𝐧𝐠 **queued** 𝐚𝐭 𝐩𝐨𝐬𝐢𝐭𝐢𝐨𝐧 {position}!")
        return await lel.delete()
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        costumer = message.from_user.mention
        await message.reply_photo(
        photo=f"{BG_IMAGE}",
        reply_markup=keyboard,
        caption=f"▶️𝑺𝑵𝑬𝑯𝑨𝑩𝑯𝑰 𝑺𝑬𝑹𝑽𝑬𝑹 𝑷𝑳𝑨𝒀𝑰𝑵𝑮 𝑺𝑶𝑵𝑮 𝑼𝑷𝑳𝑶𝑨𝑫𝑬𝑫 𝑩𝒀 @SNEHABHI_SERVER 𝐫𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝 𝐛𝐲 {costumer}"
        )
        return await lel.delete()
