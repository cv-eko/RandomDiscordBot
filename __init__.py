import discord
import asyncio
import os
import pluginloader

client = discord.Client()

@client.event
@asyncio.coroutinea
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith('!'):
        args = message.content.split( );        
        
        for i in pluginloader.getPlugins():
            
            plugin = pluginloader.loadPlugin(i)
            if(args[0][1:] == plugin.command):
                var = plugin.process(args,client)
                if(plugin.type == "message"):
                    yield from client.send_message(message.channel, var)
            
            
client.run("BOT_KEY")

