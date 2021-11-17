import asyncio
import os

import dotenv
import twitchio
from twitchio.ext import commands

dotenv.load_dotenv()


def path_exists(filename):
    return os.path.join(".", f"{filename}")


if not os.path.exists(path_exists(".env")):
    input("Please create a .env using the setup instructions in README.md")

name = input("\n\nWhat is your Twitch username? (eg: mmattbtw)\n>")

channel_name = input("What channel would you like to chat in? (eg: xqcow)\n>")


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=os.environ.get("TOKEN"),
            client_id=os.environ.get("client_id"),
            nick=name,
            prefix="don't use this prefix lmfao",
            initial_channels=[channel_name],
        )

    async def event_ready(self):
        message = input(
            "\n\nWhat message would you like to send? (eg: Hello World!)\n>"
        )

        print(f"Ready | {self.nick} | Starting auto chatting.")
        channel = self.get_channel(f"{channel_name}")
        while True:
            await asyncio.sleep(1)
            await channel.send(message)
            await asyncio.sleep(1)
            await channel.send(f"{message}  ")

    async def event_message(self, message):
        await self.handle_commands(message)


bot = Bot()
bot.run()
