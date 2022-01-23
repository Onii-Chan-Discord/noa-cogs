from redbot.core import commands, cog_manager
import random, discord, json

class BreadFact(commands.Cog):
    """Sends a random bread fact!"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def breadfact(self, ctx):
        cm = cog_manager.CogManager()
        ipath = str(await cm.install_path())
        facts = json.load(open(ipath + "/breadfact/facts.json", "r", encoding="utf-8"))
        bfint = random.randint(0,57)
        if 550984303526281219 == ctx.author.id:
            await ctx.send(facts[bfint])
        elif ctx.author.id == ctx.author.id:
            await ctx.send(facts[bfint+1])
        else: 
            return