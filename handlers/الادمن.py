from asyncio.queues import QueueEmpty
from config import que
from pyrogram import Client, filters
from pyrogram.types import Message
from cache.admins import set
from helpers.decorators import authorized_users_only, errors
from helpers.channelmusic import get_chat_id
from helpers.filters import command2, other_filters
from callsmusic import callsmusic, queues
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream


ACTV_CALLS = []

@Client.on_message(command2(["ايقاف","توقف"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    await message.delete()
    await callsmusic.pytgcalls.pause_stream(message.chat.id)
    await message.reply_text("» ᴛʀᴀᴄᴋ ᴘᴀᴜsᴇᴅ ʙʏ {} ʙᴀʙʏ😫".format( message.from_user.mention ), )


@Client.on_message(command2(["كمل","استكمال"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    await message.delete()
    await callsmusic.pytgcalls.resume_stream(message.chat.id)
    await message.reply_text("» ᴛʀᴀᴄᴋ ʀᴇsᴜᴍᴇᴅ ʙʏ {} ʙᴀʙʏ🤗".format( message.from_user.mention ), )


@Client.on_message(command2(["اسكت","انهاء"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    try:
        callsmusic.queues.clear(message.chat.id)
    except QueueEmpty:
        pass

    await message.delete()
    await callsmusic.pytgcalls.leave_group_call(message.chat.id)
    await message.reply_text("حاضر هسكت اهو🥲".format(
      message.from_user.mention ), )

@Client.on_message(command2(["تخطي"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    await message.delete()
    global que
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("» ɴᴏᴛʜɪɴɢ ɪs ᴘʟᴀʏɪɴɢ ᴡʜᴀᴛ ᴛᴏ sᴋɪᴘ ʙᴀʙʏ🥲")
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            await callsmusic.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        callsmusic.queues.get(chat_id)["file"],
                    ),
                ),
            )
    await message.reply_text("» اتخطيت المسار {} 🤔".format( message.from_user.mention ), )
