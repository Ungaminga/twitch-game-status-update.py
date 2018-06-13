# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 22:02:43 2018

@author: loljkpro
"""

def change_game_status(game, status):
    from twitch import TwitchClient
    client = TwitchClient()
    channel = client.channels.get()
    client.channels.update(channel_id=channel['id'], status=status, game=game)

def main():
    import sys
    try:
        if len(sys.argv) < 2:
            raise IOError("No data to rename")
        
        game = sys.argv[1]
        status = None if len(sys.argv) < 3 else sys.argv[2]
        change_game_status(game, status)
    except Exception as e:
        print("%s: %s"%(type(e).__name__, e))

if __name__ == "__main__":
    main()
