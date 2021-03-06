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

    lel = await message.reply("RππΊπΎ ππ°ππ° ππ°π±π°π πΊπ°ππΎ β­ ππΎπ½πΆ π³π·ππ½π³π· ππ°π·π° π·π β€οΈπ...uploaded by @SNEHABHI_SERVER  β©β")
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="π«πππΏπΏπΎπTβ¨",
                        url=f"https://t.me/SNEHABHI_SERVER"),
                    InlineKeyboardButton(
                        text="π« π²π·π°π½π½π΄π»β¨",
                        url=f"https://t.me/ABHI_NETWORK1")
                ],[

                    InlineKeyboardButton(

                           text="π« πΌπ°πππΈ πΆππΎππΏ π", url=f"https://t.me/LIVE_LIKE_LIFE")

            ],[       

                    InlineKeyboardButton(

                           text="π«πΎππ½π΄π πΊπΈπ½πΆβ¨", url=f"https://t.me/SNEHU_IS_MINE")

            ],[           

                    InlineKeyboardButton(

                           text="π«πΎππ½π΄π πππ΄π΄π½β¨", url=f"HTTP://T.ME/ABHI_IS_MINE")

                ]
            ]
        )

    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"β Videos longer than {DURATION_LIMIT} minute(s) aren't allowed to play!"
            )

        file_name = get_file_name(audio)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await lel.edit_text("πΆ Beta jao song ka nam acche se dekh kar ao.. aisa koi song nahi ha merepass π...uploaded by @SNEHABHI_SERVER β¨")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await message.reply_photo(
        photo=f"{BG_IMAGE}",
        reply_markup=keyboard,
        caption=f"#β£ ππ¨π?π« π«ππͺπ?ππ¬π­ππ π¬π¨π§π  **queued** ππ­ π©π¨π¬π’π­π’π¨π§ {position}!")
        return await lel.delete()
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        costumer = message.from_user.mention
        await message.reply_photo(
        photo=f"{BG_IMAGE}",
        reply_markup=keyboard,
        caption=f"βΆοΈπΊπ΅π¬π―π¨π©π―π° πΊπ¬πΉπ½π¬πΉ π·π³π¨ππ°π΅π? πΊπΆπ΅π? πΌπ·π³πΆπ¨π«π¬π« π©π @SNEHABHI_SERVER π«ππͺπ?ππ¬π­ππ ππ² {costumer}"
        )
        return await lel.delete()
