from pyrogram import Client, filters
from pyrogram.types import Message

from bot import OWNER_ID, COMMM_AND_PRE_FIX, BROADCAST_COMMAND
from bot.bot import Bot
from bot.hf.flifi import uszkhvis_chats_ahndler
from bot.sql.users_sql import get_chats


@Bot.on_message(
    filters.command(BROADCAST_COMMAND, COMMM_AND_PRE_FIX)
    & uszkhvis_chats_ahndler([OWNER_ID])
)
async def num_start_message(client: Bot, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to Message..`", quote=True)
    reply = message.reply_to_message
    All = get_chats()
    TTL = len(All)
    SUCCESS = 0
    for chat in All:
        try:
            await reply.copy(chat)
            SUCCESS += 1
        except Exception as e:
            print(e, chat)
    MSG = "<b>BroadCast Completed !</b>\n"
    MSG += f"<b>Succeed :</b> <code>{SUCCESS}</code> <b>Chats!</b>"
    if TTL != SUCCESS:
        MSG += f"\n<b>Failed :</b> <code>{All-SUCCESS}</code> <b>Chats.</b>"
    await message.reply_text(MSG, quote=True)
