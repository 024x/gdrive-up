# from bot.customFilters.authchecker import is_auth
# from bot.helper.utils import (is_magnet, is_url)
# import os
# from bot import (aria2, DownloadDict, DOWNLOAD_LOCATION, EDIT_TIME, LOGGER)
# from bot.ariaHelper.ariaDownload import add_url
# from bot.ariaHelper.stauts import progress
# import time


# << ------ This plugin Is Inactive Now i am handling this using regex  ------->>



# @Client.on_message(Filters.command(["leech"]))
# async def mirror(client, message):
#     current_user_id = message.from_user.id
#     uid = current_user_id
#     ID = str(message.from_user.id)
#     MsgId = message.message_id
#     new_download_location = os.path.join(
#         DOWNLOAD_LOCATION,
#         str(current_user_id),
#         str(time.time())
#     )

#     sentm = await message.reply_text(f"<code> Nothing Here </code>")

#     if message.reply_to_message:
#         repmsg = message.reply_to_message.text
#     else:
#         repmsg = None

#     if len(message.command) > 1:
#         msg = message.command[1]
#     else:
#         msg = None
# #  If user use command inline method /command https://example.com
#     if msg is not None and is_url(msg):
#         download = add_url(aria2, msg, new_download_location)
#         if download:
#             DownloadDict[uid] = download  # Download contains gid
#             print("UID:", message.from_user.id)
#             downloadComplete = await progress(aria2=aria2, gid=DownloadDict[uid], event=sentm, ID=current_user_id)

#         if downloadComplete:
#             print(downloadComplete)
#             # sentm.edit("uploading Your file")
#         else:
#             print(downloadComplete)
#             # await sentm.edit("uploading progress")

# # If User use reply methods
#     if repmsg is not None and is_url(repmsg):
#         download = add_url(aria2, repmsg, new_download_location)
#         # Download contains gid

#         if download:
#             DownloadDict[uid] = download
#             await progress(aria2, DownloadDict[uid], sentm, current_user_id)

#     # if doc is not None and document.mime_type == "application/x-bittorrent":
