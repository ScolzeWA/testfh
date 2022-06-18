import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from helpers.filters import command2, other_filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command(["سورس","السورس"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.delete()
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a6c96cdbd066ca2388d06.jpg",
        caption=f"""ᴘʀᴏɢʀᴀᴍᴍᴇʀ [𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍 ☤ ](https://t.me/WORLD_MUSIC_F) 𖡼\nᴛᴏ ᴄᴏᴍᴍụɴɪᴄᴀᴛᴇ ᴛᴏɢᴇᴛʜᴇʀ 𖡼\nғᴏʟʟᴏᴡ ᴛʜᴇ ʙụᴛᴛᴏɴѕ ʟᴏᴡᴇʀ 𖡼""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("♡اضف البوت الى مجموعتك♡", url=f"https://t.me/{bu}?startgroup=true"),
            ]
         ]
     )
  )

@Client.on_message(command(["المطور","مطور"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.delete()
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""◍ مش محتاجين نكتب كلام كتير خش ع اول زرار وانت هتعرف""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("• 𝘿𝙀𝙑𝙀𝙇𝙊𝙋𝙀𝙍 ☤ ", url=f"https://t.me/WORLD_MUSIC_F"),
            ],
            [
                InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ]
         ]
     )
  )