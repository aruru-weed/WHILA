from discord import Client, TextChannel

from AbstractCommand import AbstractCommand


class SyowaCommand(AbstractCommand):
    def __init__(self, name: str):
        self.name = name
        pass

    async def run(self, client: Client, event, args: list):
        channel: TextChannel = event.channel
        await channel.send("syowa- 放尿")
        pass
