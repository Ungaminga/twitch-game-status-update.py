# twitch-game-status-update.py
Simple script, that help you update your game and status w/o going to twitch dashboard
### Libs used: 
* [python-twitch-client](https://github.com/tsifrer/python-twitch-client)
### Usage:
1. First of all, you will create your application. Go to [dev.twitch.tv](https://dev.twitch.tv/) and create one. 
If you going to use [tokengen](https://twitchapps.com/tokengen/) (recomended) - set OAuth Redirect URL to `https://twitchapps.com/tokengen/`. 
In other cases - `http://localhost`

2. Now you need get OAuth token, i recommend you to use [tokengen](https://twitchapps.com/tokengen/). 
As `scopes` use `channel_read channel_editor`. In other cases, you can use [The official twitch dev docs](https://dev.twitch.tv/docs/authentication/).

3. Test your `client_id` and `oauth_token` using [try_config.py](https://github.com/Ungaminga/twitch-game-status-update.py/blob/master/try_config.py). Set the variables and run script.

4. Edit [.twitch.cfg](https://github.com/Ungaminga/twitch-game-status-update.py/blob/master/.twitch.cfg) and copy them to your homedir and python settings dir, if needed. My directory with python settings is `D:\WinPython\settings`. For homedir in windows type `%userprofile%` to windows explorer.
For more correct homedir finding and testing, run your python in command line and type these:
```
import os
print(os.path.expanduser('~'))
```
The output will be your homedir for running python scripts.

5. Edit [dota2.bat](https://github.com/Ungaminga/twitch-game-status-update.py/blob/master/dota2.bat) for automatic changing game and description while running game script. Debug it with cmd.

6. Happy Streaming.
