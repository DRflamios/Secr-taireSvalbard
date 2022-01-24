mport discord
import pickle
import random
import time

token = ("BOT-TOKEN")
delay = 0.1
list = ["MESSAGE"]
occurence = 1


'''
# invitelink = str(input("INVITE-LINK"))

async def on_message(message):
    print(message)
    if message.content.startswith("+raidhere"):
        for x in range(0, spamamt):
            time.sleep(1)
            for msg in list:
                await client.send_message(message.channel, msg)
                time.sleep(5)

async def on_ready():
    prin("on ready")
    await client.accept_invite(invitelink)
'''

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as: ", self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        print("Got the message: ", message.content)
        if message.author == self.user:
            return

        if message.content.startswith("+raidhere"):
            print("Raid started")
            for x in range(0, occurence):
                time.sleep(delay)
                for msg in list:
                    await message.channel.send(msg)
                    time.sleep(delay)
            print("Done")

client = MyClient()
client.run(token)
                                                                                              [ Read 49 lines ]
