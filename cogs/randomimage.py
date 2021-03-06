import discord
from discord.ext import commands
import json
import random

# Import short commands from json file
with open('./json/subreddits.json') as config:
    subreddit_list = json.load(config)


class RedditRandomImage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = self.bot.reddit
        self.subreddits_list = subreddit_list

    @commands.command()
    async def random(self, ctx, subreddit_name: str):
        try:
            img_request = self.reddit.subreddit('memes').random().url
            value = random.randint(0, 0xffffff)
            response = discord.Embed(color=value)
            response.set_image(url=img_request)

            await ctx.send(embed=response)
        except Exception as e:
            print("Got ({}) error from  {}".format(e, ctx.invoked_with))
            await ctx.send("I could not find `{}`".format(subreddit_name))

    @commands.command()
    async def e(self, ctx, message):
        elephant_gif = self.reddit.subreddit("babyelephantgifs").random().url
        await ctx.send(elephant_gif)


def setup(bot):
    bot.add_cog(RedditRandomImage(bot))
