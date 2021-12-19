""" credentials """

import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
from .get_config import get_config

# apparently, no error appears even if the path does not exists
load_dotenv("config.env")

# The Telegram API things
# Get these values from my.telegram.org or Telegram: @useTGxBot
API_HASH = get_config("API_HASH", should_prompt=True)
APP_ID = get_config("APP_ID", should_prompt=True)
# get a token from @BotFather
TOKEN = get_config("TOKEN", should_prompt=True)
# Seperate User ID who are authorized to use the bot
OWNER_ID = int(get_config(
        "OWNER_ID",
        "-100",
        should_prompt=True
    )
)

# Your Username Without @ Symbol Required
OWNER_USERNAME = get_config("OWNER_USERNAME")
# Telegraph Link Of Img When If Owner Start.
START_IMG = get_config("START_IMG")
# Telegraph Link On Img If Users Starts The Bot.
PM_IMG = get_config("PM_IMG")
# Bot Or Your Name
NAME = get_config("NAME")
# channel/chat to join before contacting
SUB_CHANNEL = get_config("SUB_CHANNEL")
# sqlalchemy Database for the bot to operate
DB_URI = get_config(
    "DATABASE_URL",
    should_prompt=True
)
# Number of update workers to use.
# 4 is the recommended (and default) amount,
# but your experience may vary.
# Note that going crazy with more workers
# wont necessarily speed up your bot,
# given the amount of sql data accesses,
# and the way python asynchronous calls work.
TG_BOT_WORKERS = int(get_config("TG_BOT_WORKERS", "4"))
#
COMMM_AND_PRE_FIX = get_config("COMMM_AND_PRE_FIX", "/")
#
BAN_COMMAND = get_config("BAN_COMMAND", "ban")
#
UN_BAN_COMMAND = get_config("UN_BAN_COMMAND", "unban")
# start command
START_COMMAND = get_config("START_COMMAND", "start")
# broadcast command
BROADCAST_COMMAND = get_config("BROADCAST_COMMAND", "broadcast")
# /start message when other users start your bot
START_OTHER_USERS_TEXT = int(get_config(
    "START_OTHER_USERS_TEXT",
    0
))
# message to indicate,
# if any message was deleted by the user
# so as to prevent replying to that message
DELETED_MESSAGES_NOTIFICATION_TEXT = get_config(
    "DELETED_MESSAGES_NOTIFICATION_TEXT",
    (
        "<b>This Message Was Deleted 🗑️</b>\n\n"
        "<b>This Is An Open Source Project Available On </b>"
        "https://github.com/AASFCYBERKING/NoPMBot\n\n\n"
        "<b>Any Issues Or Bug </b>@Aasfcyberking 🖤"
    )
)
# IDEKWBYRW
DERP_USER_S_TEXT = get_config(
    "DERP_USER_S_TEXT",
    "😐"
)
# message to show when user is banned
IS_BLACK_LIST_ED_MESSAGE_TEXT = get_config(
    "IS_BLACK_LIST_ED_MESSAGE_TEXT",
    (
        "<b>✅ You Have Been Un-Banned</b>\n\n<u>⚜️ Reason</u>: <code>{reason}</code>"
    )
)
# IDEKWBYRW
REASON_DE_LIMIT_ER = get_config(
    "REASON_DE_LIMIT_ER",
    "\n\n"
)
# message to show when user is unbanned
IS_UN_BANED_MESSAGE_TEXT = get_config(
    "IS_UN_BANED_MESSAGE_TEXT",
    (
        "<b>🚫 You Have Been Banned Forever.</b>\n\n<u>⚜️ Reason</u>: <code>{reason}</code>"
    )
)
# message to show if bot was blocked by user
BOT_WS_BLOCKED_BY_USER = get_config(
    "BOT_WS_BLOCKED_BY_USER",
    "Bot was blocked by the user."
)
# path to store LOG files
LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "NoPMsBot.log")

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_ZZGEVC,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    """ get a Logger object """
    return logging.getLogger(name)
