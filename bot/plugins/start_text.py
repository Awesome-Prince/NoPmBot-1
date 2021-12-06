from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from bot import (
    AUTH_CHANNEL,
    COMMM_AND_PRE_FIX,
    START_COMMAND
)
from bot.bot import Bot
from bot.hf.flifi import uszkhvis_chats_ahndler

START_TEXT = """
───「 <a href="https://telegra.ph/file/de0013d013b55c4676a36.jpg">AASFCYBERKING</a> 」───
<b>Hey Whassup! ,
You Can Ask Any Help Or Any Doubt Here I Will Reply You Soon As Possible</b>
➖➖➖➖➖➖➖➖➖➖➖➖➖
<code>You Can Contact @AASFCYBERKING With This Bot</code>
"""

@Bot.on_message(
    filters.command(START_COMMAND, COMMM_AND_PRE_FIX) &
    ~uszkhvis_chats_ahndler([AUTH_CHANNEL])
)
async def num_start_message(client: Bot, message: Message):
    await message.reply_text(
        client.commandi[START_COMMAND],
        quote=True
    )


@Bot.on_message(
    filters.command(START_COMMAND, COMMM_AND_PRE_FIX) &
    uszkhvis_chats_ahndler([AUTH_CHANNEL])
)
async def nimda_start_message(_, message: Message):
    await message.reply_text(
        START_TEXT,
        quote=True
    )
