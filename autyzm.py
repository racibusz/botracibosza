import discord
import asyncio
import time

class clientClass(discord.Client):
    @asyncio.coroutine
    def on_ready(self):
        print("RZECZ: {0}".format(rzecz))
        print(self.user)
    async def on_message(self, msg):
        await msg.channel.send(rzecz)
        time.sleep(0.8)

if __name__ == '__main__':
    rzecz = "https://cdn.discordapp.com/attachments/859791779045965848/860709159375863818/xdd.png"
    discord = clientClass()
    discord.run("ODYwNjk2NzQzNzI1MjM2MjQ2.YN_Cng.myG4m3kHIwLk5thlpRbf4y_CgyA", bot=False)