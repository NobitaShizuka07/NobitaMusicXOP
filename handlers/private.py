import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/d2f4189ab9cc2b93e1a26.jpg",
        caption=f"""**๐๐ก๐ข๐ฌ ๐๐ฌ ๐๐๐ฏ๐๐ง๐๐ ๐ฅ๐๐๐ฅ๐๐ ๐ซ๐๐ฆ ๐๐ฎ๐ฌ๐ข๐ ๐ถ ๐๐จ๐ญ ๐๐ฎ๐ง ๐๐ง ๐๐ซ๐ข๐ฏ๐๐ญ๐ ๐ฅ ๐๐ฉ๐ฌ ๐ซ๐๐๐ซ๐ฏ๐๐ซ ๐ ๐๐๐๐ฅ โค๏ธ ๐๐ข๐ ๐ก ๐๐ฎ๐๐ฅ๐ข๐ญ๐ฒ ๐๐ฎ๐ฌ๐ข๐ ๐ง ๐๐ง ๐๐ ๐๐๐ฏ๐๐ฅ๐จ๐ฉ๐๐ ๐๐ฒ = [แดนแดฟแญ๏ผฎ๏ผฏ๏ผข๏ผฉ๏ผด๏ผกเฟ](https://NobitaShizuka07)

๐๐ซ๐๐๐ญ๐จ๐ซ :- [โจ แดนแดฟแญ๏ผฎ๏ผฏ๏ผข๏ผฉ๏ผด๏ผกเฟ ๐](https://t.me/NobitaShizuka07)
๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญ :- [โจ ๐๐๐๐๐๐ ๐๐๐๐๐๐๐ โค๏ธ๐ธ](https://t.me/Nobita_Supports)
๐๐ข๐ฌ๐๐ฎ๐ฌ๐ฌ :- [โจ  ๐๐๐ฝ๐๐๐ผ'๐ ๐๐๐๐๐ฟ ๐ง](https://t.me/Nobita_Ki_Duniya)
๐๐จ๐ฆ๐ฆ๐๐ง๐ :- [โจ๐๐น๐ถ๐ฐ๐ธ โ๏ธ ๐ก๐ผ๐ ๐ฉ](https://telegra.ph/COMMANDS-03-19-2)
๐๐๐๐๐ข๐ง๐ '๐ :- [โจ ๐๐ผ๐ถ๐ป โค๏ธ๐ฅ](https://t.me/Nobita_Ki_Duniya)

๐๐ ๐๐จ๐ฎ ๐๐๐ฏ๐ ๐๐ง๐ฒ ๐๐ฎ๐๐ฌ๐ญ๐ข๐จ๐ง๐ฌ ๐๐ง๐ ๐๐๐ฅ๐ฉ ๐๐ก๐๐ง ๐๐ฆ ๐๐ฒ ๐๐จ๐ฌ๐ฌ = [MR.๏ผฎ๏ผฏ๏ผข๏ผฉ๏ผด๏ผกโค๏ธ](https://t.me/NobitaShizuka07)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฅ Jแดษชษด Hแดสแด & Sแดแดแดแดสแด โจ", url=f"https://t.me/Nobita_Supports")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/d2f4189ab9cc2b93e1a26.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฅ Cสษชแดแด Mแด Tแด Gแดแด Rแดแดแด ๐", url=f"https://github.com/NobitaShizuka07/NobitaMusicX")
                ]
            ]
        ),
    )
