class script(object):
    START_TXT = """👋 Hello {}
I Can Provide Movies 🥳
Just Add Me To Your Group As Admin 🤩"""

    HELP_TXT = """Help"""

    ABOUT_TXT = """★ My Name: <a href=https://t.me/{}>{}</a>
★ Creator: <a href=https://t.me/Hansaka_Anuhas>Hansaka Anuhas</a> 🇱🇰
★ Bot Server: <a href=https://www.heroku.com>Heroku</a>
★ Database: <a href=https://www.mongodb.com>MongoDB</a>"""

    FILTERS_TXT = """Filters"""

    MANUALFILTERS_TXT = """<b><u>Manual Filters</u></b>

<b>Commands and Usage:</b>
• /filter - Add Filter
• /filters - List All Filters
• /del - Delete Filter
• /delall - Delete All Filters"""

    BUTTONS_TXT = """<b><u>Buttons</u></b>

<b>URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/{})</code>

<b>Alert Buttons:</b>
<code>[Button Text](buttonalert:Alert Message)</code>"""

    AUTOFILTERS_TXT = """<b><u>Auto Filters</u></b>

<b>Usage:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
4. I'll add all the files in that channel to my database."""

    CONNECTIONS_TXT = """<b><u>Connections</u></b>

<b>Commands and Usage:</b>
• /connect - Connect PM
• /disconnect - Disconnect PM
• /connections - List All Connections"""

    EXTRAMODS_TXT = """<b><u>Extra Mods</u></b>

<b>Commands and Usage:</b>
• /id - User ID
• /info - User Information
• /imdb - IMDb Movie Information
• /search - Various Movie Information"""

    STATUS_TXT = """★ Total Files: <code>{}</code>
★ Total Users: <code>{}</code>
★ Total Chats: <code>{}</code>
★ Used Storage: <code>{}</code>
★ Free Storage: <code>{}</code>"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    REQINFO = """
⚠ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ⚠
ᴀꜰᴛᴇʀ 10 ᴍɪɴᴜᴛᴇꜱ ᴛʜɪꜱ ᴍᴇꜱꜱᴀɢᴇ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇʟᴇᴛᴇᴅ
ɪꜰ ʏᴏᴜ ᴅᴏ ɴᴏᴛ ꜱᴇᴇ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴍᴏᴠɪᴇ / sᴇʀɪᴇs ꜰɪʟᴇ, ʟᴏᴏᴋ ᴀᴛ ᴛʜᴇ ɴᴇxᴛ ᴘᴀɢᴇ
"""

    MINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ᴍᴏᴠɪᴇ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ
ᴇxᴀᴍᴘʟᴇ : Black Adam 2022
🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)
"""

    SINFO = """
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ꜱᴇʀɪᴇꜱ ʀᴇǫᴜᴇꜱᴛ ꜰᴏʀᴍᴀᴛ
⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯
ɢᴏ ᴛᴏ ɢᴏᴏɢʟᴇ ➠ ᴛʏᴘᴇ ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ ➠ ᴄᴏᴘʏ ᴄᴏʀʀᴇᴄᴛ ɴᴀᴍᴇ ➠ ᴘᴀꜱᴛᴇ ᴛʜɪꜱ ɢʀᴏᴜᴘ
ᴇxᴀᴍᴘʟᴇ : Loki S01E01 & Loki S01 E01
🚯 ᴅᴏɴᴛ ᴜꜱᴇ ➠ ':(!,./)
"""

    HOWTODOWNLOAD_TXT = """
    FIRS CLICK BUTTON"""
