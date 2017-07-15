# imports that are required for the plugin
import discord
import random
from random import shuffle 

# All plugins require a command word to be typed in
command = "user"
# The type of message that is sent back over discord.
type = "message"

# A process function is required for the plugin to run.
# It takes two argument, the first is the arguments passed from discord.
# The second is the client instance.
def process(args,client):
    # check the amount of arguments passed
    # there will always be atleast 1, which is the command itself
    if len(args) == 1:
        # go through each of the servers the bot is connected to, this should just be 1.
       for server in client.servers:
            # get the members list of the server
            membersList = list(server.members)
            # remove the bot from the members list
            membersList.remove(server.get_member_named("RandomUserBot#1105"))
            # make sure to only return members that are online
            membersList = [x for x in membersList if x.status == discord.Status.online]
            # return a random member
            return random.choice(list(membersList))
    else:
        # if the second argument is "all"
        if(args[1] == "all"):
            # go through each of the servers, there should only be 1.
            for server in client.servers:
                # add all members to a list
                membersList = list(server.members)
                # remove the bot from the list of members
                membersList.remove(server.get_member_named("RandomUserBot#1105"))
                # return a random user
                return random.choice(list(membersList))
         # if the second argument is "list"
        if(args[1] == "list"):
            # go through the servers the bot is connected to, there should only be 1.
            for server in client.servers:
                # get the member list from the server
                membersList = list(server.members)
                # remove the bot from the list of servers
                membersList.remove(server.get_member_named("RandomUserBot#1105"))
                # shuffle the list to make it random
                shuffle(membersList)
                stringlist = ""
                # for each member in the list
                for member in membersList:
                # Implement a string return that contains a list of all members
                    if member.status == discord.Status.online:
                        stringlist = stringlist + str(member) + "\n"
                return stringlist