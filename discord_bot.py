from Config import *
import discord
from discord.ext import commands

import requests
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

stiker = [":wave:",
          ":clap:",
          ":kissing_cat:",
          ":joy_cat:",
          ":heart_eyes_cat:",
          ":heart_eyes:",
          ":poop:",
          ":kissing_heart:",
          ":face_with_symbols_over_mouth:",
          ":middle_finger:",
          ":skull_crossbones:",
          ":skull:",
          ":ghost:",
          ":brain:",
          ":rofl:",
          ":cold_face:",
          ":liar:",
          ":+1:",
          ":-1:",
          ":innocent:",
          ":kiss:",
          ":writing_hand:",
          ":sewing_needle:",
          ":thread:",
          ":crown:",
          ":cut_of_meat:",
          ":jar:",
          ":rice:",
          ":hamburger:"]


@bot.event
async def on_message(message):
    word_list = message.content.split(" ")
    if message.content == "привет":
        await message.channel.send("я рад тебя видеть")
    elif message.content == "салам":
        await message.channel.send("валекум салам!")
    elif "игра" in word_list:
        await message.channel.send("кто то сказал игра?!")
    elif message.content == "сука":
        await message.channel.send("нельзя матерится!!!!!!")

    elif message.content.startswith("как дела?"):
        await message.reply("отлично, а у тебя как?", mention_author=True)
    elif message.content.startswith("хорошо"):
        await message.reply("это хорошо!", mention_author=True)

        #отсилает оприеделённый стикер
    elif message.content == "отправь мне стикер привет":
        await message.channel.send(stiker[0])
    elif message.content == "сможешь похлопать в лодоши?" or message.content == "сможешь похлопать в лодоши":
        await message.channel.send(stiker[1])
    elif message.content == "отправь мне стикер цылуюшего кота":
        await message.channel.send(stiker[2])
    elif message.content == "отправь мне стикер смеюшешося ката":
        await message.channel.send(stiker[3])
    elif message.content == "отправь мне стикер влюблённого кота":
        await message.channel.send(stiker[4])
    elif message.content == "отправь мне стикер влюблёного смайлика":
        await message.channel.send(stiker[5])
    elif message.content == "отправь мне стикер говно" or message.content == "отравь мне стикер дерьмо" or message.content == "отравь мне стикер какашка":
        await message.channel.send(stiker[6])
    elif message.content == "отправь мне стикер воздушный поцелуй":
        await message.channel.send(stiker[7])
    elif message.content == "отправь мне стикер с мотюкаюшимся смайликом":
        await message.channel.send(stiker[8])
    elif message.content == "отправь мне стикер со средним пальчиком":
        await message.channel.send(stiker[9])
    elif message.content == "отправь мне стикер череп с костями":
        await message.channel.send(stiker[10])
    elif message.content == "отправь мне стикер череп":
        await message.channel.send(stiker[11])
    elif message.content == "отправь мне стикер привидение":
        await message.channel.send(stiker[12])
    elif message.content == "отправь мне стикер мозг":
        await message.channel.send(stiker[13])
    elif message.content == "отправь мне стикер рофл":
        await message.channel.send(stiker[14])
    elif message.content == "отправь мне стикер замороженого смайлика":
        await message.channel.send(stiker[15])
    elif message.content == "отправь мне стикер любопытного смайлика":
        await message.channel.send(stiker[16])
    elif message.content == "отправь мне стикер лайк":
        await message.channel.send(stiker[17])
    elif message.content == "отправь мне стикер дизлайк":
        await message.channel.send(stiker[18])
    elif message.content == "отправь мне стикер ангел":
        await message.channel.send(stiker[19])
    elif message.content == "отправь мне стикер поцелуй":
        await message.channel.send(stiker[20])
    elif message.content == "отправь мне стикер пишущую руку":
        await message.channel.send(stiker[21])
    elif message.content == "отправь мне стикер иголку":
        await message.channel.send(stiker[22])
    elif message.content == "отправь мне стикер нитку":
        await message.channel.send(stiker[23])
    elif message.content == "отправь мне стикер корону":
        await message.channel.send(stiker[24])
    elif message.content == "отправь мне стикер резаное мясо":
        await message.channel.send(stiker[25])
    elif message.content == "отправь мне стикер банка":
        await message.channel.send(stiker[26])
    elif message.content == "отправь мне стикер миска с рисом":
        await message.channel.send(stiker[27])
    elif message.content == "отправь мне стикер бургер":
        await message.channel.send(stiker[28])


    await bot.process_commands(message)

# @bot.command()
# async def PrintADMIN(ctx):
   # Temp = []

    # await ctx.send(stiker)
   # await ctx.send(len(Temp))

@bot.command()
async def randomImg(ctx):

    temp = random.randint(1, 29)
    n = stiker[temp]
    try:
        await ctx.send(n)
    except IndexError:
        await ctx.send(n)







words = ['ПРИКОЛ', 'МЕМБРАНА', 'СТУЛ', 'СТОЛ', 'КИРПИЧ', 'СТАКАН', 'ХОЛОДИЛЬНИК', 'КОВЁР']
members = []
lives = 0
running = 'none'
current_player = 0
word = []
display_word = []
original_word = ''


@bot.command()
async def start(ctx):
    global running, members, lives
    if running != 'none':
        await ctx.send('Игра уже началась! Чтобы завершить игру - введите команду >stop')
    else:
        running = 'joining'
        members.append(ctx.author.name)
        lives = 5
        await ctx.send('Игра началась! Пишите >join, если хотите присоединиться.')


@bot.command()
async def join(ctx):
    global members

    if running == 'none':
        await ctx.send('Пока некуда присоединяться. Введите >start, чтобы начать игру.')

    elif running == 'joining':
        if ctx.author.name not in members:
            members.append(ctx.author.name)
            await ctx.send('Вы в игре!')
        else:
            await ctx.send('Вы уже в игре!')

    else:
        await ctx.send('Игра уже начата :(')


@bot.command()
async def play(ctx):
    global running, word, display_word, original_word

    if running == 'none':
        await ctx.send('Игра пока не началась. Введите >start, чтобы начать')

    elif running == 'joining':
        running = 'running'
        a = random.choice(words)
        original_word = a

        for i in a:
            word.append(i)
            display_word.append('-')

        await ctx.send(
            'Игра запущена! Загаданное слово: ' + ''.join(display_word) + ' Первым ходит ' + str(
                members[current_player]) + '. Введите команду >guess и букву.')
    else:
        await ctx.send('Игра запущена! Первым ходит ' + str(
            members[current_player]) + '. Введите команду >guess и букву.\
Загаданное слово: ' + ''.join(display_word))


@bot.command()
async def guess(ctx, letter):
    global display_word, word, current_player, running, lives

    letter = letter.upper()

    if running == 'running':
        if ctx.author.name in members:
            if ctx.author.name == members[
                current_player]:

                if letter in word:
                    while letter in word:

                        letter_index = word.index(letter)

                        display_word[letter_index] = letter
                        word[letter_index] = '*'

                    await ctx.send('Есть такая буква!')
                else:
                    lives -= 1
                    await ctx.send('Такой буквы нет :(')

                if current_player == len(members) - 1:
                    current_player = 0
                else:
                    current_player += 1

            else:
                await ctx.send('Ошибка! Сейчас ходит ' + str(members[current_player]))

        else:
            await ctx.send('Ошибка! Вы не зарегистрировались :(')

        if word.count('*') == len(
                word):
            await ctx.send('Слово отгадано, игра окончена. Чтобы начать новую - введите >start.')
            init()

        elif lives <= 0:
            await ctx.send('Слово не отгадано, а жизни кончились. Игра окончена. Чтобы начать новую - введите >start.')
            init()

        else:
            await ctx.send('Загаданное слово: ' + ' '.join(display_word) + '. Сейчас ходит ' + members[
                current_player] + '. Жизней осталось: ' + str(lives))
    elif running == 'none':
        await ctx.send('Игра пока не началась. Введите >start, чтобы начать')
    else:
        await ctx.send('Игра пока не запущена, ждем пока все подключатся. Чтобы начать игру - введите >play')


def init():
    global members, lives, running, current_player, word, display_word, original_word
    members = []
    lives = 0
    running = 'none'
    current_player = 0
    word = []
    display_word = []
    original_word = ''


@bot.command()
async def helpme(ctx):
    await ctx.send('''Приветствуем вас! У вас есть возможность сыграть в игру виселица.\n

Правила довольно просты: \n

набирается команда игроков, которая поочередно дает ответы с вариантами пропущенных букв. \n

Каждый неправильный ответ приближает команду к виселице :)''')
    await ctx.send('''Доступны команды: \n
 >start - запустить игру \n
 >join - присоединиться к игре \n
 >play - начать раунд''')


@bot.command()
async def stop(ctx):
    if running != 'none':
        await ctx.send('Игра остановлена!')
        init()







@bot.command()
async def weather(ctx, *args):

    city = args[0]
    appid = "723765522b7d4e3e682fc8e3f84d4bd1"
    lang = "ru"
    units = "metric"
    weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + appid + "&units=" + units + "&leng=" + lang)
    temp = weather.json()['main']
    temp = temp['temp']
    await ctx.send("temp: " + str(temp))


bot.run(Token)




