# create a bot
# create a class which is a bot
from twitchio.ext.commands import Bot, Context, command
import twitchio
import os

class MyCustomBot(twitchio.Client): # MyCustomBot is a Bot
    
    # overriding constructor
    def __init__(self):
        super().__init__(
            token=os.environ['TMI_TOKEN'],
            initial_channels=['ultimateminds']
        )

    @command()                      # Decorator ->
    async def hello(self, ctx: Context):
        args = ctx.message.content.split(" ")
        print(args[1:])

    async def event_ready(self):   # overriden so we do not call it
        print("Bot is ready")

    async def event_reward_redeem(self, reward, user):
        print(f'{user.display_name} redeemed {reward.title} ({reward.cost} points)')
        
        if reward.id == 'your_reward_id':
            # do something when the specific reward is redeemed
            pass

o = MyCustomBot()
o.run()

