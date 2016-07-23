from time import strftime
import discord
import asyncio
client = discord.Client()

user='__USER__'
passwd='__PASS__'

alias={
    '81253444156915712': "Me"
}

ignore={
    '159800228088774656': "AIRHORN SOLUTIONS"
}

chan={
    'afk': '204442851210297344',
    'target': '205153248657670144'
}


def thetime():
    return strftime('%Y-%m-%d %H:%M:%S')

@client.event
async def on_ready():
    global chan
    chan['target'] = client.get_channel(chan['target'])
    client.get_all_channels()
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_voice_state_update(before, after):
    if before.id in ignore.keys():
        return
    if before.id in alias.keys():
        after.name, before.name = alias[before.id], alias[before.id]
    if (after.self_deaf or after.deaf):
        if not (before.self_deaf or before.deaf):
            if before.voice_channel:            
                print('%s> %s deafened' %(thetime(),after.name))
                await client.send_message(chan['target'], '%s, deafened' %(after.name))
                return
    if (before.self_deaf or before.deaf):
        if not (after.self_deaf or after.deaf):
            print('%s> %s undeafened' %(thetime(),after.name))
            await client.send_message(chan['target'], '%s, un deafened' %(after.name))
            return
    if (after.self_mute or after.mute):
        if not (before.self_mute or before.mute):
            if after.voice_channel.id == chan['afk']:
                return
            print('%s> %s muted' %(thetime(),after.name))
            await client.send_message(chan['target'], '%s, muted' %(after.name))
            return
    if (before.self_mute or before.mute):
        if not (after.self_mute or after.mute):
            print('%s> %s unmuted' %(thetime(),after.name))
            await client.send_message(chan['target'], '%s, un muted' %(after.name))
            return
    if not before.voice_channel and after.voice_channel:
        print('%s> %s joined %s' % (thetime(),after.name,after.voice_channel.name))
        await client.send_message(chan['target'], '%s, joined %s' % (after.name,after.voice_channel.name))
        return
    if not after.voice_channel and before.voice_channel:
        print('%s> %s left' % (thetime(),before.name))
        await client.send_message(chan['target'], '%s, left' % (before.name))
        return
    if after.voice_channel and before.voice_channel:
        if not after.voice_channel.id == before.voice_channel.id:
            print('%s> %s moved to %s' % (thetime(),before.name,after.voice_channel.name))
            await client.send_message(chan['target'], '%s, moved to, %s' % (before.name,after.voice_channel.name))

client.run(user, passwd)
