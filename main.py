import discord as dc

from AbstractCommand import AbstractCommand
from SyowaCommand import SyowaCommand

DISCORD_TOKEN = "ODI2NzI3MjI0NjA2NDU3ODY2.YGQrug.O0cuWSRCqWT1k8ZzJYBJAeImTjc"

PRE_FIX = "<w>"

client = dc.Client()

commands: list = list()

print("start")


def debug(s: str):
    print(s)


def add_command(command):
    if issubclass(type(command), AbstractCommand):
        commands.append(command)
        print("enable" + command.name)
        pass
    pass


@client.event
async def on_message(event):
    message: str = str(event.content)
    debug(message + " : " + message[:len(PRE_FIX)])
    # message がコマンドか確認
    if message[:len(PRE_FIX)] != PRE_FIX:
        return
    if message <= PRE_FIX:
        return
    message: str = message[len(PRE_FIX):]
    # コマンド だけ抽出
    per_space: list = message.split(" ")
    label: str = per_space[0]
    args: list = per_space[1:]

    for command in commands:
        command: AbstractCommand = command
        debug(label + " == " + command.name)
        if command.name == label:
            await command.run(client, event, args)


# コマンド追加
add_command(SyowaCommand("syowa"))

client.run(DISCORD_TOKEN)
