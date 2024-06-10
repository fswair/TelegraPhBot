import os
from PIL import Image
from telegraph import upload_file
from telethon import TelegramClient, events
from telethon.tl.types import Document, MessageMediaPhoto, MessageMediaDocument
from config import API_ID, API_HASH, BOT_TOKEN, HELP_TEXT, STRING
from utils import post_to_telegraph, buttons, run_sync
from telethon.sessions import StringSession


client = TelegramClient(StringSession(STRING), API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@client.on(events.NewMessage(pattern='/start'))
@client.on(events.NewMessage(pattern='/help'))
async def t_ph_help(event):
    await event.respond(
        HELP_TEXT.format(
            mention=event.sender.first_name
        ),
        link_preview=False
    )

@client.on(events.NewMessage(pattern='/telegraph'))
async def _telegraph(event):
    r = await event.get_reply_message()
    if not r:
        return await event.respond("Lütfen bir medyaya veya metne yanıt verin!")

    msg = await event.respond("İşleniyor...")

    LIMIT = 5242880

    if (
        (isinstance(r.media, MessageMediaPhoto) and r.photo.sizes[0].size <= LIMIT) or
        (isinstance(r.media, MessageMediaDocument) and r.document.mime_type in ["image/gif", "video/mp4", "image/jpeg", "image/png", "text/html", "text/plain", "application/x-python"] and r.document.size <= LIMIT) or
        r.raw_text or
        (r.sticker and r.sticker.mime_type == "image/webp")
    ):
        await msg.edit("Telegra.ph ya yükleniyor...")
        m_text = event.message.text
        title = m_text.split(maxsplit=1)[1].strip() if " " in m_text or "\n" in m_text else ""
        if not title:
            title = event.sender.first_name

        if r.raw_text or (r.document and r.document.mime_type in ["text/html", "text/plain", "application/x-python"]):
            if r.document:
                path = await client.download_media(r, "download/")
                with open(path, "r") as f:
                    text = f.read()
                os.remove(path)
                text = f"""<pre><code class="{r.document.mime_type.split('/')[-1]}">{text}</code></pre>"""
            else:
                text = r.raw_text
        else:
            path = await client.download_media(r, "download/")
            if r.sticker:
                img = Image.open(path).convert('RGB')
                os.remove(path)
                img.save(f"download/sticker.png", "png")
                path = "download/sticker.png"

            response = await run_sync(upload_file, path)
            os.remove(path)

            url = f"https://telegra.ph{response[0]}"
            text = f"<img src='{url}'/>"

        text += f"<br><br>{r.message if r.message else ''}"
        url = await run_sync(
            post_to_telegraph,
            from_user=event.sender,
            title=title,
            text=text.replace("\n", "<br>")
        )
        await event.respond(
            f"**Kopyala:** `{url}`",
            buttons=buttons(url),
            link_preview=False
        )
        await msg.delete()
    else:
        await msg.edit("Desteklenmeyen tür veya boyut 5mb den fazla.")

client.start()
client.run_until_disconnected()
