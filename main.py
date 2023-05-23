import discord
import os
from dotenv import load_dotenv
load_dotenv()

people = [609068698791313421, 1105861447709376544, 812416647934902312, 354546286634074115]

class Item():
    def __init__(self, name, starting_bid, duration):
        self.name = name
        self.starting_bid = starting_bid
        self.duration = duration
    def Getinfo(self):
        return f"The item", self.name, f"has a starting bid of", self.starting_bid, f"and will be auctioned for", self.duration, f"seconds"

client = discord.Client(intents=discord.Intents.all())
tree = discord.app_commands.CommandTree(client)

class Auction(discord.app_commands.Group):
    def __init__(self, client):
        super().__init__(name='auction', description='Auction commands')
        self.client = client
    
    @discord.app_commands.command(name='create', description='Create an auction')
    async def create(self, interation: discord.Interaction, item: str, starting_bid: int, duration: int):
        await interation.response.send_message("Creating an auction...")
        item1 = Item(item, starting_bid, duration)
        await interation.followup.send(item1.Getinfo())
        

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Auctionable, your mom is"))
    auction_group = Auction(client)
    tree.add_command(auction_group)
    await tree.sync()
    print('Commands synced')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('ping farzaan'):
        for i in range(25):
            await message.channel.send('Hey <@1105861447709376544>')
    if message.content.startswith('ping eeshanya'):
        for i in range(25):
            await message.channel.send('Hey <@812416647934902312>')
    if message.content.startswith('!shutdown') and message.author.id in people:
        await message.channel.send('Shutting down...')
        await message.channel.send('Bye Bye :)')
        await client.close()

@tree.command(name='ping', description='Pong!')
async def ping(interation: discord.Interaction, message: str = "AHHHHHH!!"):
    embed = discord.Embed(title='Pong!', description=f'{round(client.latency * 1000)}ms', color=0x00ff00)
    embed.set_footer(text=message)
    await interation.response.send_message(embed=embed)
    
@tree.command(name="spamping", description="Spam ping someone")
async def spamping(interation: discord.Interaction, user: discord.User, amount: int = 10):
    await interation.response.send_message(f'Hey {user.mention}')
    for i in range(amount-1):
        await interation.followup.send(f'Hey {user.mention}')

"""@tree.command(name = "shutdown", description = "Shuts down the bot")
async def shutdown(interation: discord.Interaction):
    await interation.response.send_message("Shutting down...")
    await interation.followup.send("Bye Bye :)")
    await client.close()"""
    
client.run(os.getenv('TOKEN'))