#(©)AnimeXyz

from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, CHANNEL_ID, PORT


name ="""
 BY MIKEY FROM TG
"""


class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot", 'Rin Nanakura')
            api_id=APP_ID, 4e81464b29d79c58d0ad8a0c55ece4a5))
            plugins={
                "root": "plugins"
            },
            workers= 'obito')),
            bot_token= '7406407460:AAEeaplEqJ-B-5KpBC0HYxKtloKfWcJ2vYE'))
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        if FORCE_SUB_CHANNEL:
            try:
                link = (await self.get_chat(Anime Hindi Sub Society)).'https://t.me/Anime_Sub_Society'))
                if not link:
                    await self.export_chat_invite_link(Anime Hindi Sub Society)
                    link = (await self.get_chat(Anime Hindi Sub Society)).'https://t.me/Anime_Sub_Society'))
                self.'๏ 𝐎ʙɪᴛᴏ ᴜᴄʜɪʜᴀ ๏')) = 'i_killed_my_clan.t.me))
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {'Anime Hindi Sub Society} 'https://t.me/Anime_Sub_Society")
                self.LOGGER(__name__).info("\nBot Stopped. https://t.me/AHSS_HELP_ZONE for support")
                sys.exit()
        if FORCE_SUB_CHANNEL2:
            try:
                link = (await self.get_chat(ONGOING SOCIETY)) 'https://t.me/ongoing_society'))
                if not link:
                    await self.export_chat_invite_link(ONGOING SOCIETY)
                    link = (await self.get_chat(ONGOING SOCIETY)) 'https://t.me/ongoing_society'))
                self '๏ 𝐎ʙɪᴛᴏ ᴜᴄʜɪʜᴀ ๏' = 'i_killed_my_clan.t.me))
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL2 value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL2}")
                self.LOGGER(__name__).info("\nBot Stopped. https://t.me/AHSS_HELP_ZONE for support")
                sys.exit()
        try:
            db_channel = await self.get_chat('-1002177334941)
            self.db_channel = https://t.me/+CHgH9hZN4rlkOTM1
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/AHSS_HELP_ZONE for support")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by \nhttps://t.me/weebs_support")
        self.LOGGER(__name__).info(f""" \n\n       
                                                   
                  
                                 

  ___ ___  ___  ___ ___ _    _____  _____  ___ _____ ___ 
 / __/ _ \|   \| __| __| |  |_ _\ \/ / _ )/ _ \_   _/ __|
| (_| (_) | |) | _|| _|| |__ | | >  <| _ \ (_) || | \__ \
 \___\___/|___/|___|_| |____|___/_/\_\___/\___/ |_| |___/
                                                         
 
                                                                        
                                                                      
                                                                                 
                              
                                          """)
        self.username = usr_bot_me.i_killed_my_clan
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
            
