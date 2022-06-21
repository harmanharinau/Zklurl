# (c) @PredatorHackerzZ

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "PHListBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is a TeleGram BotList Search Bot of @CyniteBots And Some Other Bots Available On TeleGram.

🤖 My Name: <a href='https://t.me/LiveTVChannelBot'> ʟɪᴠᴇ ᴄʜᴀɴɴᴇʟ sᴛʀᴇᴀᴍᴇʀ </a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram </a>

📡 Server: <a href='https://heroku.com'> Heroku </a>

👨‍💻 Modified By: <a href='https://t.me/CyniteBots'>ᴄʏɴɪᴛᴇ-ʙᴏᴛs</a>

🌀 Youtube: <a href='https://youtube.com/channel/UCiaz-J50QhtJ73XEEjP_aLQ'>ᴄʟɪᴄᴋ ᴍᴇ</a>

👥 Bots Support: <a href='https://t.me/CyniteOfficial'>ᴄʏɴɪᴛᴇ</a>

📢 Bots Updates: <a href='https://t.me/CyniteBots'>ᴄʏɴɪᴛᴇ-ʙᴏᴛs</a></b>
"""
    
    ABOUT_HELP_TEXT = """<b>👨‍💻 Developers : <a href='https://t.me/CyniteOfficial'>ᴄʏɴɪᴛᴇ-ᴏғғɪᴄɪᴀʟ</a>

Bots are simply Telegram accounts operated by software – not people – and they'll often have AI features. They can do anything – teach, play, search, broadcast, remind, connect, integrate with other services, or even pass commands to the Internet of Things.

🌀 I will help you to find Live Tv Channels.

🌀 If you Get Any Error In Searching Please Report at **@Cyniteofficial**.

🌀 Our Project Channel: <a href='https://t.me/Cynitebots'>ᴄʏɴɪᴛᴇ-ʙᴏᴛs</a>.

🌀 All Bots Based On Users and Developer Demands. 

🤖 Join For All Available Bots On Telegram: @CyniteBots.
"""
    
    HOME_TEXT = """
<b>👋 Hey !{}, I am TV Streamer Bot <a href='https://t.me/cyniteBots/4523'>ᴄʏɴɪᴛᴇ</a>.

<a> Modified By : @Cyniteofficial</a>

       <a> Credits goes to Everyone Who Supported.</b>

<a> Made With ❤ By @CyniteOfficial </a>
"""


    START_MSG = """
<b>👋 Hey {}, ᴍʏ <a href='https://telegra.ph/Channel-List-By-CyniteBots-06-21'>ᴄʜᴀɴɴᴇʟ ʟɪsᴛ</a>.
<a> I can generate streaming Channel links</a>
"""
    ADD_BOTS = """<b>Heya! {} Want Same Like This Then Contact The Support.</b>"""
