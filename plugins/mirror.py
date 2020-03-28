from bot.helper.utils import (is_magnet, is_url)
import os
from bot import (aria2, DownloadDict, DOWNLOAD_LOCATION,
                 EDIT_TIME, LOGGER, Creds_path)
from bot.ariaHelper.ariaDownload import add_url
from bot.ariaHelper.stauts import progress
import time
from pyrogram import  Client ,Filters,ContinuePropagation
import aiohttp
from bot.customFilters.authchecker import is_auth


@Client.on_message(Filters.regex(r"^(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+")& is_auth())
async def direct_link_checker_async(flt, m):
    url = m.text.strip()
    if url.endswith("m3u8"):
        return False
    LOGGER.info(f"Direct Link Checker : {url}")
    requests = aiohttp.ClientSession()
    h = await requests.head(url, allow_redirects=True)
    content_type = h.content_type
    await requests.close()
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


async def mirror(client, message):
    is_direct = await direct_link_checker_async(client, message)
    if not is_direct:
        print("Not direct link")
        raise ContinuePropagation
    current_user_id = message.from_user.id
    uid = current_user_id

    ID = str(message.from_user.id)
    message.message_id
    new_download_location = os.path.join(
        DOWNLOAD_LOCATION,
        str(current_user_id),
        str(time.time())
    )
    # if os.path.isfile(os.path.join(Creds_path, ID)):
    
    sentm = await message.reply_text(f"<code> Processing Your Uri ...</code>")

    msg = message.text.strip()
    msg = msg.split(" ")[-1]

    if msg is not None and is_url(msg):
        download = await add_url(aria2, msg, new_download_location)
        if download:
            DownloadDict[uid] = download  # Download contains gid
            print("UID:", message.from_user.id)
            await progress(aria2=aria2, gid=DownloadDict[uid], event=sentm, ID=current_user_id)
    
        # await message.reply_text("You Are Not Authorised use /login 😞")
