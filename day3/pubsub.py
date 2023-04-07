import twitchio
import os
from twitchio.ext import pubsub


users_oauth_token = os.environ['TOKEN']
my_token = f"oauth:{users_oauth_token}"

users_channel_id = 134136350
client = twitchio.Client(token=my_token)
client.pubsub = pubsub.PubSubPool(client)

@client.event()
async def event_pubsub_bits(event: pubsub.PubSubBitsMessage):
    pass # do stuff on bit redemptions

@client.event()
async def event_pubsub_channel_points(event: pubsub.PubSubChannelPointsMessage):
    print(f"{event.reward.id} {event.reward.cost} {event.reward.prompt} {event.input}")
    print(f"{event.user.id} {event.user.name}")
    followings = await event.user.fetch_following(users_oauth_token)
    is_following = any((f for f in followings if f.to_user.id == users_channel_id))
    
    # subscriptions = await event.user.fetch_subscriptions(users_oauth_token)
    # # if_subscriber = any((f for f in subscriptions if f.user.i == users_channel_id))
    print(is_following)

@client.event()
async def event_pubsub_channel_subscriptions(event):
    print(event)

async def main():
    topics = [
        pubsub.channel_points(users_oauth_token)[users_channel_id],
        pubsub.bits(users_oauth_token)[users_channel_id],
        pubsub.channel_subscriptions(users_oauth_token)[users_channel_id]
    ]
    await client.pubsub.subscribe_topics(topics)
    await client.start()

client.loop.run_until_complete(main())