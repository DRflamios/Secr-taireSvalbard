
import discord
import pickle
import random
import time
from discord.utils import get

token = ("OTM0NTQ3NzI2Mzc5NjYzNDcx.YexrZQ.PE7nMmvTneRyGxTwYgHlmjr9cgY")
delay = 0.1
list1 = ["Personne à spammer"]
list2 = ["Salut!"]
list3 = ["Demande envoyé, vous pouvez attendre dans le salon vocal d'aide le temps qu'un assistant vous rejoint."]
list4 = ["Je suis le secrétaire du Svalbard, je m'occupe d'acceuillir les nouveaux, prévenir si une personne demande de l'aide dans le salon tickets et plein d'autres taches."]
occurence = 1



'''
# invitelink = str(input("dqq9vV7A"))

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
                for msg in list1:
                    await message.channel.send(msg)
                    time.sleep(delay)
            print("Done")

        if message.content.startswith("+hey"):
            print("Réponse")
            for x in range(0, occurence):
                time.sleep(delay)
                for msg in list2:
                    await message.channel.send(msg)
                    time.sleep(delay)
            print("Done")

        if message.content.startswith("+qui-est-tu"):
            print("Présentation")
            for x in range(0, occurence):
                time.sleep(delay)
                for msg in list4:
                    await message.channel.send(msg)
                    time.sleep(delay)
            print("Done")

        if message.content.startswith("+assist"):
            print("Envoie de la demande")
                        for x in range(0, occurence):
                time.sleep(delay)
                for msg in list3:
                    await message.channel.send(msg)
                    time.sleep(delay)
                    channel = client.get_channel(938405541548539935)
                    mention = message.author.mention
                    await channel.send(f"<@&938404968464023552> : {mention} a besoin d'aide.")
            print("Done")

        if message.content.startswith("+help"):
            print("Envoie de la demande")
            for x in range(0, occurence):
                time.sleep(delay)
                await message.channel.send(f"Liste de commandes disponibles: \n +help \n +hey \n +assist (uniquement dans le salon tickets) \n +qui-est-tu")

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Bienvenue {member.mention} au {guild.name}! Un membre du pays va venir de prendre en charge.'
            await guild.system_channel.send(to_send)

intents = discord.Intents.default()
intents.members = True
