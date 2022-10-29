#Imports
from aiogram import Bot, Dispatcher, executor, types
import random
import asyncio
import db
import markup as nav

#Start bot
bot = Bot(token="5700642711:AAFkz7gTymGySSOGUiSjskQE_9Fm6T7K9-4", parse_mode="html")
dp = Dispatcher(bot)


#Create Data Base
db.CreateDB()

@dp.message_handler(commands='start')
async def start(message):
    await bot.send_sticker(chat_id=message.from_user.id,
                           sticker=r"CAACAgIAAxkBAAEEtoZifVbPDYz-LyFOSd6XYfCUSGPb1wACOAsAAk7kmUsysUfS2U-M0CQE")
    await message.reply(f'<b>Приветствую тебя!</b> <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>\n\n'
        f'▫️ <b>Выбирай свою роль в этой игре!</b>\n\n'
        f'▫️ <b>Роль можно будет сменить нажав /start</b>\n\n'
        f'▫️ <b>Команда:</b> /help <b>- выдаст список вседоступных команд</b>\n\n', reply_markup = nav.persMenu)
        
@dp.message_handler(commands='help')
async def help(message):
    await message.reply("<b>скоро</b>")
    
    #при выборе мента
@dp.message_handler(lambda msg: msg.text.startswith('Ментяра'))
async def ment(message):
    await message.reply(f'Вы выбрали честную и доблестную жизнь!', reply_markup = nav.mentMenu)
    return
    #патруль города
cooldown = []
@dp.message_handler(lambda msg: msg.text.startswith('Патруль города'))
async def jerk(message):
    db.cursor.execute(f"SELECT name FROM users where id = {message.from_user.id}")
    if db.cursor.fetchone() == None:
        db.InsertValue(message.from_user.first_name, message.from_user.id)
    if message.from_user.id in cooldown:
        for row in db.cursor.execute(f"SELECT work FROM users where id={message.from_user.id}"):
            await message.answer(f'<b>⚠️Ваша смена еще не пришла!</b>\n\n'
                f'<b>🏦На твоем счету денег:</b> {row[0]}ⓜ\n\n'
                f'<b>⚙️Попробуй через минуту!</b>')
        return
    select = random.randint(1, 3)
    if select == 1 or select == 3:
        plus = random.randint(1, 1000)
        db.UpdateValue('work', plus, message.from_user.id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT work FROM users where id={message.from_user.id}"):
            await message.reply(f'✅ <b>Вы удачно пропатрулировали город!\nПришла зарплата: +</b>{plus}ⓜ\n\n'
                f'🏦<b>Ваш баланс:</b> {row[0]}ⓜ\n\n'
                f'⚙️<b>Ваша смена окончена, приходите через минуту!</b>')
    elif select == 2:
        minus = random.randint(1, 200)
        db.UpdateValueMinus('work', minus, message.from_user.id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT work FROM users where id={message.from_user.id}"):
            await message.reply(f'🔥 <b>О нет! Машина сломалась при патрулировании!\nВы оплатили ремонт за свой счет: -</b>{minus}ⓜ\n\n'
                f'🏦<b>Ваш баланс:</b> {row[0]}ⓜ\n\n'
                f'⚙️<b>Машину чинят, попробуй патрулирвоать через минуту!</b>')
    cooldown.append(message.from_user.id)
    await asyncio.sleep(60)
    cooldown.remove(message.from_user.id)
    #пост
@dp.message_handler(lambda msg: msg.text.startswith('Пост'))
async def jerk(message):
    db.cursor.execute(f"SELECT name FROM users where id = {message.from_user.id}")
    if db.cursor.fetchone() == None:
        db.InsertValue(message.from_user.first_name, message.from_user.id)
    if message.from_user.id in cooldown:
        for row in db.cursor.execute(f"SELECT work FROM users where id={message.from_user.id}"):
            await message.answer(f'<b>⚠️Ваша смена еще не пришла!</b>\n\n'
                f'<b>🏦На твоем счету денег:</b> {row[0]}ⓜ\n\n'
                f'<b>⚙️Попробуй через минуту!</b>')
        return
    select = random.randint(1, 3)
    if select == 1 or select == 3:
        plus = random.randint(1, 235)
        db.UpdateValue('work', plus, message.from_user.id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT work FROM users where id={message.from_user.id}"):
            await message.reply(f'✅ <b>Вы удачно простоял пост!\nПришла зарплата: +</b>{plus}ⓜ\n\n'
                f'🏦<b>Ваш баланс:</b> {row[0]}ⓜ\n\n'
                f'⚙️<b>Ваша смена окончена, приходите через минуту!</b>')
    elif select == 2:
        minus = random.randint(1, 100)
        db.UpdateValueMinus('work', minus, message.from_user.id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT work FROM users where id={message.from_user.id}"):
            await message.reply(f'🔥 <b>О нет! К вам ворвались грабители с оружием!\nУ вас забрали что было в кошельке: -</b>{minus}ⓜ\n\n'
                f'🏦<b>Ваш баланс:</b> {row[0]}ⓜ\n\n'
                f'⚙️<b>Попробуй стоять на посту через минуту!</b>')
    cooldown.append(message.from_user.id)
    await asyncio.sleep(60)
    cooldown.remove(message.from_user.id)
    
    #при выборе хацкера
@dp.message_handler(lambda msg: msg.text.startswith('Хакер'))
async def ment(message):
    await message.reply(f'Вы выбрали тёмную сторону!', reply_markup = nav.hackerMenu)
    return
    #Взламываем пентагон
cooldown = []
@dp.message_handler(lambda msg: msg.text.startswith('Патруль города'))
async def jerk(message):
    db.cursor.execute(f"SELECT name FROM users where id = {message.from_user.id}")
    if db.cursor.fetchone() == None:
        db.InsertValue(message.from_user.first_name, message.from_user.id)
    if message.from_user.id in cooldown:
        for row in db.cursor.execute(f"SELECT work FROM users where id={message.from_user.id}"):
            await message.answer(f'<b>⚠️Вы еще не залягли на дно после прошлого</b>\n\n'
                f'<b>🏦На твоем счету денег:</b> {row[0]}ⓜ\n\n'
                f'<b>⚙️Попробуй через минуту!</b>')
        return
    select = random.randint(1, 3)
    if select == 1 or select == 3:
        plus = random.randint(1, 25000)
        db.UpdateValue('work', plus, message.from_user.id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT work FROM users where id={message.from_user.id}"):
            await message.reply(f'✅ <b>Вы удачно взломали пентагон!\nВаш доход: +</b>{plus}ⓜ\n\n'
                f'🏦<b>Ваш баланс:</b> {row[0]}ⓜ\n\n'
                f'⚙️<b>Вы решили залечь на дно, приходите через минуту!</b>')
    elif select == 2:
        minus = random.randint(1, 30000)
        db.UpdateValueMinus('work', minus, message.from_user.id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT work FROM users where id={message.from_user.id}"):
            await message.reply(f'🔥 <b>О нет! Вас вычеслили!\nУ вас изъяли крупную сумму денег: -</b>{minus}ⓜ\n\n'
                f'🏦<b>разработчик @drenix_x\n\nВаш баланс:</b> {row[0]}ⓜ\n\n'
                f'⚙️<b>Вы в тюрьме, попробуй  через минуту!</b>')
    cooldown.append(message.from_user.id)
    await asyncio.sleep(60)
    cooldown.remove(message.from_user.id)
    
@dp.message_handler(lambda msg: msg.text.startswith('Взломать банк'))
async def jerk(message):
    db.cursor.execute(f"SELECT name FROM users where id = {message.from_user.id}")
    if db.cursor.fetchone() == None:
        db.InsertValue(message.from_user.first_name, message.from_user.id)
    if message.from_user.id in cooldown:
        for row in db.cursor.execute(f"SELECT work FROM users where id={message.from_user.id}"):
            await message.answer(f'<b>⚠️Вы на дне.</b>\n\n'
                f'<b>🏦На твоем счету денег:</b> {row[0]}ⓜ\n\n'
                f'<b>⚙️Попробуй через минуту!</b>')
        return
    select = random.randint(1, 3)
    if select == 1 or select == 3:
        plus = random.randint(1, 200000)
        db.UpdateValue('work', plus, message.from_user.id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT work FROM users where id={message.from_user.id}"):
            await message.reply(f'✅ <b>Вы успешно взломали банк!\nВы перевели себе: +</b>{plus}ⓜ\n\n'
                f'🏦<b>Ваш баланс:</b> {row[0]}ⓜ\n\n'
                f'⚙️<b>Вы решили залечь на дно, продолжайте через минуту!</b>')
    elif select == 2:
        minus = random.randint(1, 350000)
        db.UpdateValueMinus('work', minus, message.from_user.id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT work FROM users where id={message.from_user.id}"):
            await message.reply(f'🔥 <b>О нет! Вас арестовали!\nУ изъяли крупную сумму бабок: -</b>{minus}ⓜ\n\n'
                f'🏦<b>Ваш баланс:</b> {row[0]}ⓜ\n\n'
                f'⚙️<b>Вы в тюрьме, попробуйте через минуту!</b>')
    cooldown.append(message.from_user.id)
    await asyncio.sleep(60)
    cooldown.remove(message.from_user.id)
    
    
    #при выборе майнинга
@dp.message_handler(lambda msg: msg.text.startswith('Майнер'))
async def ment(message):
    await message.reply(f'Вы выбрали светлую сторону заработка!', reply_markup = nav.mainMenu)
    return
    

#Working
cooldown = []
@dp.message_handler(lambda msg: msg.text.startswith('Майнить'))
async def jerk(message):
    db.cursor.execute(f"SELECT name FROM users where id = {message.from_user.id}")
    if db.cursor.fetchone() == None:
        db.InsertValue(message.from_user.first_name, message.from_user.id)
    if message.from_user.id in cooldown:
        for row in db.cursor.execute(f"SELECT work FROM users where id={message.from_user.id}"):
            await message.answer(f'<b>⚠️Ты уже майнил!</b>\n\n'
                f'<b>🏦На твоем счету коинов:</b> {row[0]}ⓜ\n\n'
                f'<b>⚙️Попробуй запустить через минуту!</b>')
        return
    select = random.randint(1, 3)
    if select == 1 or select == 3:
        plus = random.randint(1, 150000)
        db.UpdateValue('work', plus, message.from_user.id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT work FROM users where id={message.from_user.id}"):
            await message.reply(f'✅ <b>Ты удачно помайнил! И за это время твоя машина заработала: +</b>{plus}ⓜ\n\n'
                f'🏦<b>На твоем счету коинов:</b> {row[0]}ⓜ\n\n'
                f'⚙️<b>Машине надо отдохнуть, попробуй запустить через минуту!</b>')
    elif select == 2:
        minus = random.randint(1, 100000)
        db.UpdateValueMinus('work', minus, message.from_user.id)
        db.con.commit()
        for row in db.cursor.execute(f"SELECT work FROM users where id={message.from_user.id}"):
            await message.reply(f'🔥 <b>О нет! Майнинг накрылся и машина сломалась. На этом ты потерял: -</b>{minus}ⓜ\n\n'
                f'🏦<b>На твоем счету коинов:</b> {row[0]}ⓜ\n\n'
                f'⚙️<b>Машине надо починить, попробуй запустить через минуту!</b>')
    cooldown.append(message.from_user.id)
    await asyncio.sleep(60)
    cooldown.remove(message.from_user.id)

#Dashboard
@dp.message_handler(lambda msg: msg.text.startswith('🏆Топ'))
async def top(message):
    db.cursor.execute(f"SELECT name, work FROM users ORDER BY work DESC LIMIT 10")
    leadermsg = "<b>   🏆Топ 10 игроков:</b>\n\n"
    fetchleader = db.cursor.fetchall()
    for i in fetchleader:
        leadermsg += f"{fetchleader.index(i) + 1}. {i[0]}:  {i[1]}ⓜ\n"
    await message.reply(str(leadermsg))

#About
@dp.message_handler(lambda msg: msg.text.startswith('📕О боте'))
async def top(message):
    await message.reply('<b>❕Информация:</b>\n▂▂▂▂▂▂▂▂▂▂▂▂▂\n<b>🧠Разрабчик: </b>@drenix_x\n<b>👤Поддержка: </b>@drenix_x')
#Polling
executor.start_polling(dp, skip_updates=True)