from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Keyboards
btnWork = KeyboardButton("💻Майнить")
btnTop = KeyboardButton("🏆Топ")
btnAbout = KeyboardButton("📕О боте")
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnWork, btnTop, btnAbout)
#выбор перса
btnMent = KeyboardButton('Ментяра')
btnHacker = KeyboardButton('Хакер')
btnMainer = KeyboardButton('Майнер')
persMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnMent, btnHacker, btnMainer)

#если выбрал мента добавляем его клаву
btnPat = KeyboardButton('Патруль города')
btnPost = KeyboardButton('Пост')
mentMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnPat, btnPost, btnTop, btnAbout)

#Если выбрал бандюгу делаем что и с ментом
btnHack = KeyboardButton('Взломать пентагон')
btnWor = KeyboardButton('Взломать банк')
hackerMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnHack, btnWor, btnTop, btnAbout)