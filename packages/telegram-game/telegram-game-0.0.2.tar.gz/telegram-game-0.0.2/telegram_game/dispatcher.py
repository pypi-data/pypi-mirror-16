"""Message dispatching logic"""

import asyncio
import aiohttp
import logging
import os

from telegram_game.api import BotAPI


logger = logging.getLogger(__name__)


class GameDispatcher():

    def __init__(self, game_class, api_token=None, queue_maxsize=5, loop=None):

        self.game_class = game_class

        if api_token is None:
            api_token = os.environ['TELEGRAM_TOKEN']

        self.queue_maxsize = 5

        if loop is None:
            loop = asyncio.get_event_loop()

        self.loop = loop

        self.http = aiohttp.ClientSession(loop=loop)
        self.api = BotAPI(api_token, self.http)

        self.queues = {}

    async def run(self):
        await self.game_class.prepare(self.loop)
        info = await self.api.getMe()
        logger.info("Starting bot: %s", info)
        await self.poll_get_updates()

    async def poll_get_updates(self):
        while True:
            updates = await self.api.getUpdates(timeout=30.)
            for i in updates:
                self.loop.create_task(self.dispatch_update(i))

    async def dispatch_update(self, update):

        if 'message' in update:

            chat_id = update['message']['chat']['id']
            msg = update['message']
            logger.info('#%d @%s: %s', chat_id,
                        msg.get('from', {}).get('username'),
                        msg.get('text', 'NO_TEXT')[:60].replace('\n', '\\n'))

            if chat_id not in self.queues:
                queue = asyncio.Queue(self.queue_maxsize)
                self.queues[chat_id] = queue
                game = self.game_class(
                    chat_id,
                    queue,
                    self.api
                )
                self.loop.create_task(game())

            try:
                self.queues[chat_id].put_nowait(update)
            except asyncio.QueueFull:
                logger.warning('QueueFull for %s', chat_id)
                self.loop.create_task(
                    self.api.sendMessage(
                        chat_id, 'Not so fast!',
                        reply_to_message_id=update['message']['message_id']
                    )
                )

        else:
            logger.warning("Unsupported update type: %s", update)
