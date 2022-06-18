import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━
اهـلا يـبـنـي.؟ {message.from_user.mention()} !
مـرحبآ بـك انــا بــوت اقـوم بــتـشـغـيـل الاغــانــي فـي الـمـڪـالـمـه الـصـوتـية .🤔❤؟
يمكنني التشغيل بصوت رائع وبدون اي مشاكل او تقطيع في الاغنيه
 +اضفني الى مجموعتك وارفعني رول بشڪل مع ڪامل الصلاحيات
 البوت يشتغل بالاوامر عربي وانجليزي
 لانضمام الحساب المساعد لتشغيل البوت اكتب انضم


  لمعرفة استخدامي بشڪل صحيح اضغط علي زر الاوامر. 🤔𝑫𝑬𝑽 [𝑾𝑶𝑹𝑳𝑫 𝑴𝑼𝑺𝑰𝑪 💗ˣ](t.me/WORLD_MUSIC_F)
━━━━━━━━━━━━━━━━━━**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ضيـف البـوت لمجمـوعتـك ✅",
                        url=f"https://t.me/{bu}?startgroup=true"
                    )
                ],
                [
                     InlineKeyboardButton(
                        "الاوامر", url=f"https://telegra.ph/%F0%9D%99%B2%E1%B4%8F%E1%B4%8D%E1%B4%8D%E1%B4%80%C9%B4%E1%B4%85s-04-06"),
                    InlineKeyboardButton(
                        "مطور البوت", url=f"https://t.me/WORLD_MUSIC_F"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 جروب الدعم", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "📣 قناة البوت", url=f"https://t.me/{Ch_World_Music}"
                    ),
                ],
            ]
        ),
    )


@Client.on_message(command(["source"]) & filters.group & ~filters.edited)
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

@Client.on_message(command(["developer","dev"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.delete()
    await message.reply_photo(
        photo=f"{DEV_PHOTO}",
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
