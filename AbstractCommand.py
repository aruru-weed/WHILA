from abc import ABCMeta, abstractmethod

from discord import Client, Message


class AbstractCommand:
    name: str

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    async def run(self, client: Client, event: Message, args: list):
        pass
