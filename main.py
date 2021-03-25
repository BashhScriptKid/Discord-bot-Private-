import discord
import os
import requests
import json
import time
import asyncio
import sys
import re
 
from keep_alive import keep_alive

client = discord.Client()

client = MyClient()
     client.run('NzY1MjQyNTQ3NDQyMDI0NDQ4.X4R9qA.b0zvSPn1Otf-uNlOwvoRHdMKnQ0')


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as NzY1MjQyNTQ3NDQyMDI0NDQ4.X4R9qA.4tN4ToX87UOHFvcXpY6mQolkwpY!'.format(self.user))
        time.sleep(3)
    async def on_message(self, message):
        print('Message from Terminal.exe: Welcome'.format(message))


import logging

logging.basicConfig(level=logging.INFO)

@client.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(
	    'Hi {member.name}, welcome to Lindows Community!')

if message.content.startswith('$help'):
		embedVar = discord.Embed(
		    title="$help <:Owner:696371112388591617->",
		    description="Shows All Of The command This Bot Has!",
		    color=0x39ff14)
		embedVar.add_field(
		    name="$help",
		    value=
		    "We are sorry,this bot currently are in development stage,so this bot haven't have any commands yet.",
		    inline=False)
		  
		  



