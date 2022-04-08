import discord
from discord import Client

class MyBot(Client):
    def __init__(self):
        super().__init__()
        self.run("OTU4Njg5Mzc1MDg3MTEyMjUy.YkQ_Dg.sSs_XmhlThJe3hlzok8HZVei1vc")

    # Renvoie au terminal le message dès que le bot est connecté
    async def on_ready(self):
        print("Coucou je suis connecté ;)")

    # Répond "Pong" lorsqu'on écrit "Ping"
    async def on_message(ctx, message):
        if message.content == "Ping":
            await message.channel.send("Pong")

    # Signaler la connexion d'un utilisateur du serveur
    default_intents = discord.Intents.default()
    default_intents.members = True
    client = discord.Client(intents=default_intents)

    async def (member):
    print(f"L'utilisateur {member.display_name} vient de se connecter !")

