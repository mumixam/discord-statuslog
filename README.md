# discord-statuslog

This script uses discord.py (https://github.com/Rapptz/discord.py) to logs events like user joined, muted, switched, left to a text channel


The dict variable `alias` forces a userid to always have the selected name, good for fixing phonetic tts   
The dict variable `ignore` will ignore all actions by that userid, the value has no effect is and just used as a comment   
The dict variable `chan` contains the channel id of the afk channel (voice) and the the target channel (text) of where the messages will be sent   
