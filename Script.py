class script(object):
    START_TXT = """<b>Hello {},

𝗛𝗜 𝗜 𝗔𝗠 𝗔 𝗦𝗨𝗣𝗘𝗥 𝗔𝗨𝗧𝗢𝗙𝗜𝗟𝗧𝗘𝗥 𝗕𝗢𝗧 𝗩𝟯+𝗩𝟰 𝗜 𝗖𝗔𝗡 𝗣𝗥𝗢𝗩𝗜𝗗𝗘 𝗠𝗢𝗩𝗜𝗘𝗦 𝗜𝗡 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗚𝗥𝗢𝗨𝗣𝗦....\n\n𝗝𝗨𝗦𝗧 𝗔𝗗𝗗 𝗠𝗘 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 𝗔𝗡𝗗 𝗘𝗡𝗝𝗢𝗬 😍\n\n👨‍💻 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 : <a href='https://telegram.dog/KOT_FREE_DE_LA_HOYA_OFF'>✯°• Kᴏᴛ Fʀᴇᴇ Dᴇ Lᴀ Hᴏʏᴀ Oғғ °•✯ | ✪ Bᴏᴛs CʀᴇᴀᴛᴏR ✪</a></b>"""
    HELP_TXT = """<b>Bruh {}
Here Is The Help For My Commands</b>."""
    ABOUT_TXT = """<b>
🤖 My Name : <a href='https://telegram.dog/KOT_MOVIES_FILTER_BOT'>KOT THALAPATHY BOT 👑</a>
 
👨‍💻 Developer : <a href='https://telegram.dog/KOT_FREE_DE_LA_HOYA_OFF'>✯°• Kᴏᴛ Fʀᴇᴇ Dᴇ Lᴀ Hᴏʏᴀ Oғғ °•✯ | ✪ Bᴏᴛs CʀᴇᴀᴛᴏR ✪</a>
  
📌 Credits : <a href='https://telegram.dog/KOT_LINKS_TEAM'>KOT LINKS TEAM</a> & <a href='https://t.me/KOT_DEVELOPERS'>KOT Team</a>
  
📡 Server : <a href='https://Heroku.com'>Heroku</a>
  
📕 Library : <a href='https://Pyrogram.com'>Pyrogram</a>
  
📦 Source Code : <a href='https://telegram.dog/KOT_SOURCE_CODE'>Click Here</a>
  
📢 Updates Channel : <a href='https://telegram.dog/KOT_BOTS'>@KOT_BOTS</a>
  
📮 Powerded By : <a href='https://telegram.dog/KING_OF_THE_CARTOONS_CHANNEL'>@KOT_CARTOONS_</a></b>
"""
    SOURCE_TXT = """<b>NOTE:</b>
- KOT THALAPATHY VIJAY is a open source project. 
- Source - https://t.me/KOT_SOURCE_CODE

<b>DEVS:</b>
- <a href=https://t.me/KOT_DEVELOPERS>KOT Team</a>"""
    MANUELFILTER_TXT = """<b>Help : Manual Filters
    
    - Filter Is The Feature Were Users Can Set Automated Replies For A Particular Keyword And Tessa Will Respond Whenever A Keyword Is Found The Message

NOTE :
---> @KOT_MOVIES_FILTER_BOT Should Have Admin Privillage / Rights !!! 
---> Only Admins Can Add Filters In A Chat...
---> Alert Buttons Have A Limit Of 64 Characters...

Commands And Usage :
• /filter - <code>Add A Filter In Chat</code>
• /filters - <code>List All The Filters Of A Chat</code>
• /del - <code>Delete A Specific Filter In Chat</code>
• /delall - <code>Delete The Whole Filters In A Chat ( Chat Owner Only )</code></b>"""
    BUTTON_TXT = """<b>Help : Buttons

- @KOT_MOVIES_FILTER_BOT Supports Both Url And Alert Inline Buttons.

NOTE :
---> Telegram Will Not Allows You To Send Buttons Without Any Content, So Content Is Mandatory.
---> @KOT_MOVIES_FILTER_BOT Supports Buttons With Any Telegram Media Type.
---> Buttons Should Be Properly Parsed As Markdown Format

URL Buttons :
<code>[Button Text](buttonurl:https://telegram.dog/KOT_BOTS)</code>

Alert buttons :
<code>[Button Text](buttonalert:This Is An Alert Message)</code></b>"""
    CONNECTION_TXT = """<b>Help : Connections

- Used To Connect Bot To PM For Managing Filters 
- It Helps To Avoid Spamming In Groups.

NOTE :
---> Only Admins Can Add A Connection.
---> Send <code>/connect</code> For Connecting Me To Ur PM

Commands And Usage :
• /connect  - <code>Connect A Particular Chat To Your PM</code>
• /disconnect  - <code>Disconnect From A Chat</code>
• /connections - <code>List All Your Connections</code></b>"""
    EXTRAMOD_TXT = """<b>Help : Extra Modules

Commands And Usage :
• /id - <code>Get Id Of A Specifed User.</code>
• /info  - <code>Get Information About A User.</code>
• /imdb  - <code>Get The Film Information From IMDB Source.</code>
• /search  - <code>Get The Film Information From Various Sources.</code></b>"""
    ADMIN_TXT = """<b>Help : Admin mods

NOTE :
This Module Only Works For My Admins

Commands and Usage :
• /logs - <code>To Get The Rescent Errors</code>
• /stats - <code>To Get Status Of Files In Db.</code>
• /users - <code>To Get List Of My Users And Ids.</code>
• /chats - <code>To Get List Of The My Chats and Ids </code>
• /leave  - <code>To Leave From A Chat.</code>
• /disable  -  <code>Do Disable A Chat.</code>
• /ban  - <code>To Ban a User.</code>
• /unban  - <code>To Unban a User.</code>
• /channel - <code>To Get List Of Total Connected Channels</code>
• /broadcast - <code>To Broadcast a Message To All Users</code></b>"""
    STATUS_TXT = """<b>--> Total Files</b> : <code>{}</code>
<b>--> Total Users</b> : <code>{}</code>
<b>--> Total Chats</b> : <code>{}</code>
<b>--> Used Storage</b> : <code>{}</code> MIB
<b>--> Free Storage</b> : <code>{}</code> MIB"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
