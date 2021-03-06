from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import authorized_users_only
from config import BOT_NAME, BOT_USERNAME, OWNER_NAME, UPDATES_CHANNEL, SUPPORT_GROUP, ASSISTANT_NAME
from modules.play import cb_admin_check


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
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
                        "๐๐จ๐ฐ ๐๐จ ๐๐ฌ๐?๐", callback_data="cbhowtouse"
                    )
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
                        "๐ซ๐พ๐๐ฝ๐ด๐ ๐บ๐ธ๐ฝ๐ถโจ", url="https://t.me/SNEHU_IS_MINE"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )





@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐๐จ๐ฐ ๐๐จ ๐๐ฌ๐ ๐๐โ:

1.) ๊ฐษชส๊ฑแด, แดแดแด แดแด แดแด สแดแดส ษขสแดแดแด.
2.) แดสแดษด แดสแดแดแดแดแด แดแด แด๊ฑ แดแดแดษชษด แดษดแด ษขษชแด แด แดสส แดแดสแดษช๊ฑ๊ฑษชแดษด๊ฑ แดxแดแดแดแด แดษดแดษดสแดแดแด๊ฑ แดแดแดษชษด.
3.) แดแดแด @{ASSISTANT_NAME} แดแด สแดแดส ษขสแดแดแด แดส แดสแดแด /userbotjoin แดแด ษชษดแด ษชแดแด สษชแด.
4.) แดแดสษด แดษด แดสแด แด แดษชแดแด แดสแดแด ๊ฐษชส๊ฑแด สแด๊ฐแดสแด ๊ฑแดแดสแด แดแด แดสแดส แดแด๊ฑษชแด.

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ค๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ", url=f"https://t.me/SNEHABHI_SERVER"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ ๐๐น๐ผ๐๐ฒ", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**๐๐ฒ๐ฟ๐ฒ ๐ถ๐ ๐๐ต๐ฒ ๐๐ผ๐ป๐๐ฟ๐ผ๐น ๐ ๐ฒ๐ป๐ ๐ข๐ณ ๐๐ผ๐:**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โธ ๐๐๐ฎ๐ฌ๐๐!", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "โถ๏ธ ๐๐๐ฌ๐ฎ๐ฆ๐๐!", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "โฉ ๐๐ค๐ข๐ฉ!", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "โน ๐๐ง๐!", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ ๐๐น๐ผ๐๐ฒ", callback_data="close"
                    )
                ]
            ]
        )
    )




@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐๐จ๐ฐ ๐๐จ ๐๐ฌ๐ ๐๐โ:

1.) ๊ฐษชส๊ฑแด, แดแดแด แดแด แดแด สแดแดส ษขสแดแดแด.
2.) แดสแดษด แดสแดแดแดแดแด แดแด แด๊ฑ แดแดแดษชษด แดษดแด ษขษชแด แด แดสส แดแดสแดษช๊ฑ๊ฑษชแดษด๊ฑ แดxแดแดแดแด แดษดแดษดสแดแดแด๊ฑ แดแดแดษชษด.
3.) แดแดแด @{ASSISTANT_NAME} แดแด สแดแดส ษขสแดแดแด แดส แดสแดแด /userbotjoin แดแด ษชษดแด ษชแดแด สษชแด.
4.) แดแดสษด แดษด แดสแด แด แดษชแดแด แดสแดแด ๊ฐษชส๊ฑแด สแด๊ฐแดสแด ๊ฑแดแดสแด แดแด แดสแดส แดแด๊ฑษชแด.

""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐๐๐น๐ผ๐๐ฒ", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
