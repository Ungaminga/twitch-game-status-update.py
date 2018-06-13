# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:41:20 2018

@author: loljkpro
"""

from twitch import TwitchClient
client = TwitchClient(client_id="client_id", oauth_token="oauth_token")
channel = client.channels.get()
print(channel)
