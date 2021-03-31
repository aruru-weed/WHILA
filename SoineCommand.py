from discord import Client, TextChannel, Message, User, DMChannel

from AbstractCommand import AbstractCommand


class SoineCommand(AbstractCommand):
    def __init__(self, name: str):
        self.name = name
        pass

    async def run(self, client: Client, event: Message, args: list):
        channel: TextChannel = event.channel
        user: User = event.author
        dm: DMChannel = await user.create_dm()
        await dm.send("おやすみ❤")
        pass
