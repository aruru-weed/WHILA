from discord import Client, TextChannel, Message

from AbstractCommand import AbstractCommand


class SNSCommand(AbstractCommand):
    def __init__(self, name: str):
        self.name = name
        pass

    async def run(self, client: Client, event: Message, args: list):
        channel: TextChannel = event.channel
        await channel.send("https:/syowatan.com")
        pass
