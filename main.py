from openai import OpenAI
import os
from dotenv import load_dotenv

import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

load_dotenv()

@bot.event
async def on_ready():
    print(f'{bot.user} 이름의 양승원T가 접속했어요...')

@bot.command(name='yang')
async def talk(ctx, *args):
    user = ctx.author
    if user.bot:
        return
    text = ''.join(args)
    prompt = text
    try:
        bot_answer = TalkWithYang(prompt)
        await ctx.send(bot_answer)
    except:
        await ctx.send('오류가 발생했어요... 미안합니다...!!!')

def TalkWithYang(message: str):
    client = OpenAI(api_key=os.environ.get('API_KEY'))
    prompt = open('prompt.txt', 'r').read()
    print(message + "라는 내용으로 gpt-4에게 전달중...!!!")
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": message}
        ],
        model='gpt-4-1106-preview',
    )
    print(chat_completion.choices[0].message.content, "라는 내용으로 gpt-4로부터 응답을 받았어요...!!!")
    return chat_completion.choices[0].message.content

bot.run(os.environ.get('DISCORD_BOT_KEY'))