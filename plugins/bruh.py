from pyrogram import Client, Filters


@Client.on_message(Filters.command(["bruh"]))
async def start(client, message):
    helptxt = f"What Do You Want Bruh.....😂 If You Need Anything Contact @BLuVDS"
    await message.reply_text(helptxt)
