import discord

global P
P = "!"

async def selfpurge(message, newcontent, mode):
    content = newcontent.split(' ')
    channel = message.channel

    try:
        await message.delete()
    except:
        pass

    if len(content) == 1:
        limit = None
    elif len(content) == 2:
        try:
            limit = int(content[1])
        except:
            bad_word = str(content[1])
            limit = None
    elif len(content) == 3:
        try:
            bad_word = str(content[1])
            limit = int(content[2])
        except:
            bad_word = str(content[2])
            limit = int(content[1])
    else:
        print("Incorrect arguments!")
        return


    if mode == "all":
        count = 0
        if (limit == None):
            async for msg in channel.history(limit=None):
                if (msg.author.id == client.user.id) and (msg.type == discord.MessageType.default):
                    await msg.delete()
                    count +=1
                else:
                    pass
        else:
            async for msg in channel.history(limit=None):
                if (msg.author.id == client.user.id) and (msg.type == discord.MessageType.default) and (count < limit):
                    await msg.delete()
                    count += 1
                elif (count >= limit):
                    break


    elif mode == "word":
        count = 0
        if (limit == None):
            async for msg in channel.history(limit=None):
                if (msg.author.id == client.user.id) and (msg.type == discord.MessageType.default) and (bad_word in msg.content):
                    await msg.delete()
                    count += 1
                else:
                    pass
        else:
            async for msg in channel.history(limit=None):
                if (msg.author.id == client.user.id) and (msg.type == discord.MessageType.default) and (bad_word in msg.content) and (count < limit):
                    await msg.delete()
                    count += 1
                elif (count >= limit):
                    break

    if isinstance(message.channel, discord.DMChannel):
        print(f"\nDeleted {count} messages in {message.channel.recipient}'s DMs.\nChannel ID: {message.channel.id}")
    else:
        print(f"\nDeleted {count} messages in {message.guild}.\nChannel name: {message.channel.name}\nChannel ID: {message.channel.id}")

      
class MyClient(discord.Client):
  async def on_connect(self):
    print("Ready to go! User: " + str(self.user.name))

  async def on_message(self, message):
    if message.author == self.user:
      content = message.content
      if content.startswith(str(P) + "purge"):
        newcontent = content.replace((str(P)), "")
        await selfpurge(message, newcontent, "all")
      elif content.startswith(str(P) + "pword"):
        newcontent = content.replace((str(P)), "")
        await selfpurge(message, newcontent, "word")


client = MyClient()
client.run("token.", bot=False)