#(©)botspciety @team_society
# Ask Doubt on telegram @i_killed_my_clan

# Clone Code Credit : YT - @taem_society / TG - @team_society / GitHub - @umaidahmad01

import sys, glob, importlib, logging, logging.config, pytz, asyncio
from pathlib import Path

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

from pyrogram import Client, idle 
from pyromod import listen
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import *
from utils import temp
from typing import Union, Optional, AsyncGenerator
from Script import script 
from datetime import date, datetime 
from aiohttp import web
from plugins import web_server
from plugins.clone import restart_bots

from TechVJ.bot import TechVJBot
from TechVJ.util.keepalive import ping_server
from TechVJ.bot.clients import initialize_clients

ppath = "plugins/*.py"
files = glob.glob(ppath)
TechVJBot.start()
loop = asyncio.get_event_loop()


async def start():
    print('\n')
    print('Initalizing Your Bot')
    bot_info = await TechVJBot.get_me()
    await initialize_clients()
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            plugins_dir = Path(f"plugins/{plugin_name}.py")
            import_path = "plugins.{}".format(plugin_name)
            spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
            sys.modules["plugins." + plugin_name] = load
            print("Tech VJ Imported => " + plugin_name)
    if ON_HEROKU:
        asyncio.create_task(ping_server())
    b_users, b_chats = await db.get_banned()
    temp.BANNED_USERS = b_users
    temp.BANNED_CHATS = b_chats
    await Media.ensure_indexes()
    me = await TechVJBot.get_me()
    temp.BOT = TechVJBot
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    logging.info(LOG_STR)
    logging.info(script.LOGO)
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    time = now.strftime("%H:%M:%S %p")
    await TechVJBot.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(today, time))
    if CLONE_MODE == True:
        print("Restarting All Clone Bots.......")
        await restart_bots()
        print("Restarted All Clone Bots.")
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app, bind_address, PORT).start()
    await idle()

        if FORCESUB_CHANNEL:
            try:
                link = (await self.get_chat(FORCESUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCESUB_CHANNEL)
                    link = (await self.get_chat(FORCESUB_CHANNEL)).invite_link
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCESUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCESUB_CHANNEL}")
                self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/weebs_support for support")
                sys.exit()
        if FORCESUB_CHANNEL2:
            try:
                link = (await self.get_chat(FORCESUB_CHANNEL2)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCESUB_CHANNEL2)
                    link = (await self.get_chat(FORCESUB_CHANNEL2)).invite_link
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCESUB_CHANNEL2 value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCESUB_CHANNEL2}")
                self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/weebs_support for support")
                sys.exit()
        if FORCESUB_CHANNEL3:
            try:
                link = (await self.get_chat(FORCESUB_CHANNEL3)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCESUB_CHANNEL3)
                    link = (await self.get_chat(FORCESUB_CHANNEL3)).invite_link
                self.invitelink3 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCESUB_CHANNEL3 value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCESUB_CHANNEL3}")
                self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/weebs_support for support")
                sys.exit()       
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/weebs_support for support")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by \nhttps://t.me/Animes_X_Hunters")
        self.LOGGER(__name__).info(f""" \n\n       

  _____ ____  _____  ______ ______ _      _______   ______   ____ _______ _____ 
 / ____/ __ \|  __ \|  ____|  ____| |    |_   _\ \ / /  _ \ / __ \__   __/ ____|
| |   | |  | | |  | | |__  | |__  | |      | |  \ V /| |_) | |  | | | | | (___  
| |   | |  | | |  | |  __| |  __| | |      | |   > < |  _ <| |  | | | |  \___ \ 
| |___| |__| | |__| | |____| |    | |____ _| |_ / . \| |_) | |__| | | |  ____) |
 \_____\____/|_____/|______|_|    |______|_____/_/ \_\____/ \____/  |_| |_____/ 
                                                                                
                                                                                
                                          """)
        self.username = usr_bot_me.username
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
