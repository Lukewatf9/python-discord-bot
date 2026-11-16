import discord
from discord import app_commands
import os
import operator
import random


token = os.environ["DISCORD_TOKEN"]
intents = discord.Intents.default()
intents.message_content = True



class MyClient(discord.Client):
    
    def __init__(self, intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
    
    
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        print("Servers:", [(guild.name, guild.id) for guild in self.guilds])

    async def on_message(self, message):
        if message.author == self.user:
            return

        print(f'Message from {message.author}: {message.content}')

        if message.content.startswith('!hello'):
            await message.channel.send(f'Hello, {message.author.mention}')
        
        if self.user in message.mentions:
            user_message = message.content
            operations = {
                "+": operator.add,
                "-": operator.sub,
                "/": operator.truediv,
                "*": operator.mul,
            }
            for symbol, calculate in operations.items():
                
                if symbol in user_message:
                    clean_string = user_message.removeprefix(str(self.user.mention)).strip()
                    numbers = [num.strip() for num in clean_string.split(symbol)]
                    num1, num2 = numbers[0], numbers[1]
                    result = calculate(float(num1), float(num2))
                    await message.channel.send(f"{num1}{symbol}{num2} = {result}")
                    return
                
            await message.channel.send(f"👀")
  

client = MyClient(intents=intents)

        
@client.tree.command(name="hello", description="Say hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Hello, {interaction.user.mention}!"
)
    
@client.tree.command(name="cba", description="Say the alphabet backwards")
async def cba(interaction: discord.Interaction):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reversed_alphabet = ""
    for i in range(len(alphabet) - 1, -1, -1):
        reversed_alphabet += alphabet[i]
    
    await interaction.response.send_message(reversed_alphabet.upper())

@client.tree.command(name="roll", description="roll a dice ")
async def roll(interaction: discord.Interaction, sides: int = 6):
    if sides <= 1:
        await interaction.response.send_message(f"{interaction.user.mention} When has a dice had {sides} sides... ")
        await interaction.followup.send(f"Sides changed to 6 ...")
        sides = 6
        result = random.randint(1,sides)
        await interaction.followup.send(f"🎲 {interaction.user.mention} just rolled {result} on a {sides}-sided dice ")
    result = random.randint(1,sides)
    await interaction.response.send_message(f"🎲 {interaction.user.mention} just rolled {result} on a {sides}-sided dice ")
    
    
client.run(token)
