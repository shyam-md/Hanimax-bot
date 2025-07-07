
import asyncio
import os
import logging
from logging.handlers import RotatingFileHandler


#Bot token @Botfather, --⚠️ REQUIRED--
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7467602116:AAEuzsmXOFFBqU7Wa1EEyMBMrG3p2b0I6ZE")

#Your API ID from my.telegram.org, --⚠️ REQUIRED--
APP_ID = int(os.environ.get("APP_ID", "26166161"))

#Your API Hash from my.telegram.org, --⚠️ REQUIRED--
API_HASH = os.environ.get("API_HASH", "b15f46991b55eda97417f78f5b6fe0c0")

#Your db channel Id --⚠️ REQUIRED--
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002879384835"))

#OWNER ID --⚠️ REQUIRED--
OWNER_ID = int(os.environ.get("OWNER_ID", "7357629115"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database --⚠️ REQUIRED--
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://jddhanush85:jayaraman143@cluster0.cmj1w.mongodb.net/?retryWrites=true&w=majority")

DB_NAME = os.environ.get("DATABASE_NAME", "adbotv2XlightXtest")

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#Collection of pics for Bot // #Optional but atleast one pic link should be replaced if you don't want predefined links
PICS = (os.environ.get("PICS", "https://vault.pictures/p/1006408b848f4b3f86be4f77e2a6361d https://vault.pictures/p/c3881749cf924e17a50f1b877e93b544 https://vault.pictures/p/50761ace57644f9f8eccdbb1a741e255 https://vault.pictures/p/a29f091e7fcc4e8ea3021822a8360ced https://vault.pictures/p/e6bda085615344f894c8a1f85ec338a6 https://vault.pictures/p/13615e4a7b224d258813200c24c0983e https://vault.pictures/p/8dbb100447dd446da85801dae30e715f https://vault.pictures/p/9d7debd0df2f46a29b085abc0ef4455f https://vault.pictures/p/48388e63b06c4197a4212020a62feed5 https://vault.pictures/p/26cc403b0d384d5186ca96100560fa63 ")).split() 

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
