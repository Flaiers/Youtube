import random, kb

from bot import unknown
from aiogram import types
from states import Lk, Save
from create import create_link
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# хэндлер на команду start
@dp.message_handler(CommandStart())
async def start(message: types.Message):
	button_youtube0 = InlineKeyboardButton('Подписаться', url='t.me/joinchat/R1Ct6BRjHCkO_AYO')
	inline_youtube0 = InlineKeyboardMarkup(row_width=1).add(button_youtube0)

	await message.answer('Подпишись на наш канал — Скачать Видео Ютуб в котором мы постим обновления бота, выкладываем интеремную информацию в сфере IT, а также устраиваем розыгрыши!\n\n'
		'Мы будем очень благодарны тебе 🥰',
		reply_markup=inline_youtube0)
	
	await message.answer('Перейди в Главное меню, чтобы Скачать видео\n'
		'PS: Нажми на кнопку внизу 👇',
		reply_markup=kb.reply_main)

# хэндлер сообщений
@dp.message_handler()
async def message(message: types.Message):
	if message.text == '🏠 Главное меню':
		await message.answer('Ты находишься в Главном меню\n'
			'Чтобы скачать видео, нажми 💾 Скачать видео\n'
			'Зайти в ЛК, нажми 📰 Личный кабинет\n'
			'Есть вопрос, нажми на кнопку ниже',
			reply_markup=kb.reply_menu)

	elif message.text == '💾 Скачать видео':
		await message.answer('Выбери тип, откуда ты хочешь отправить ссылку и придерживайся инструкции!',
			reply_markup=kb.reply_device)

	elif message.text == '📱 Приложение':
		await message.answer('Как отправить ссылку из приложения:\n'
			'Ты можешь нажать на значок поделиться, который находится под видеороликом и затем выбрать Telegram\n\n'
			'Жду ссылку от тебя)',
			reply_markup=kb.reply_back)
		await Save.app.set()

	elif message.text == '🖥 Cайт':
		await message.answer('Как отправить ссылку с сайта:\n'
			'1) Ты можешь скопировать её из адресной строки браузера и отправить мне\n'
			'2) Ты можешь нажать на значок поделиться, который находится под видеороликом и затем выбрать Telegram\n\n'
			'Жду ссылку от тебя)',
			reply_markup=kb.reply_back)
		await Save.site.set()

	elif message.text == '💻 Мобильная версия сайта':
		await message.answer('Как отправить ссылку с мобильной версии сайта:\n'
			'1) Ты можешь скопировать её из адресной строки мобильного браузера и отправить мне\n'
			'2) Ты можешь нажать на значок поделиться, который находится под видеороликом и затем выбрать Telegram\n\n'
			'Жду ссылку от тебя)',
			reply_markup=kb.reply_back)
		await Save.msite.set()

	elif message.text == '🔄 Скачать ещё раз':
		await message.answer('Выбери тип, откуда ты хочешь отправить ссылку и придерживайся инструкции!',
			reply_markup=kb.reply_device)

	elif message.text == '📰 Личный кабинет':
		await message.answer('Ты зашёл в Личный кабинет, в разделе\n'
			'📚 Наши каналы можно подписаться за вознаграждение. Заработанные кристаллы можно увидеть в разделе 💎 Мои кристаллы',
			reply_markup=kb.reply_lk)
		await Lk.choice.set()

	elif message.text == '💬 Служба поддержки':
		await message.answer('⬇️ По всем вопросам сюда ⬇️\n'
			'                   t.me/Flaiers',
			reply_markup=kb.reply_main)

	elif message.text == '⬅️ Назад':
		await message.answer('Ты зашёл в Личный кабинет, в разделе\n'
			'📚 Наши каналы можно подписаться за вознаграждение. Заработанные кристаллы можно увидеть в разделе 💎 Мои кристаллы',
			reply_markup=kb.reply_lk)
		await Lk.choice.set()

	else:
		await message.answer(random.choice(unknown),
			reply_markup=kb.reply_menu)

# хэндлер личного кабинета
@dp.message_handler(state=Lk.choice)
async def lk(message: types.Message, state: FSMContext):
	lk = message.text
	async with state.proxy() as data:
		data['lk_request'] = lk
		choice = data['lk_request']
		if choice == '💎 Мои кристаллы':
			button_sell = InlineKeyboardButton('Обмен кристаллов', callback_data='sell')
			inline_sell = InlineKeyboardMarkup(row_width=1).add(button_sell)
			try:
				user_channel = await bot.get_chat_member(chat_id=-1001196469736, user_id=message.from_user.id)
				if user_channel["status"] == 'left':
					"""для тех кто не подписался"""
					await message.answer('У тебя на счету 💳:\n'
						f'— 0 💎',
						reply_markup=inline_sell)

					await message.answer('Нажми на 👆, чтобы обменять 💎. Хочешь вернуться в Личный кабинет, нажми Назад',
						reply_markup=kb.reply_back)
					await state.reset_state()

				else:
					"""для тех кто подписался"""
					await message.answer('У тебя на счету 💳:\n'
						f'— 100 💎',
						reply_markup=inline_sell)

					await message.answer('Нажми на 👆, чтобы обменять 💎. Хочешь вернуться в Личный кабинет, нажми Назад',
						reply_markup=kb.reply_back)
					await state.reset_state()

			except:
				await message.answer('У тебя на счету 💳:\n'
					f'— 0 💎',
					reply_markup=inline_sell)

				await message.answer('Нажми на 👆, чтобы обменять 💎. Хочешь вернуться в Личный кабинет, нажми Назад',
					reply_markup=kb.reply_back)
				await state.reset_state()

		elif choice == '📚 Наши каналы':
			await message.answer('Подписавшись на наши каналы, ты получаешь кристаллы. '
				'Эти кристаллы можно будет обменивать на различные подписки, бонусы и скидки',
				reply_markup=kb.reply_back)

			button_fla = InlineKeyboardButton('Скачать Видео Ютуб', url='t.me/joinchat/R1Ct6BRjHCkO_AYO')
			button_fla_check = InlineKeyboardButton('✅ Проверить', callback_data='fla_check')
			inline_fla = InlineKeyboardMarkup(row_width=2).add(button_fla, button_fla_check)
			await message.answer('Наш канал — Скачать Видео Ютуб в котором мы постим обновления бота, выкладываем интеремную информацию в сфере IT, а также устраиваем розыгрыши!',
				reply_markup=inline_fla)

			await state.reset_state()

		elif choice == '🏠 Главное меню':
			await message.answer('Ты находишься в главном меню\n'
			'Чтобы скачать видео, нажми 💾 Скачать видео\n'
			'Зайти в ЛК, нажми 📰 Личный кабинет\n'
			'Есть вопрос, нажми на кнопку ниже',
				reply_markup=kb.reply_menu)
			await state.reset_state()

		else:
			await message.answer(random.choice(unknown),
				reply_markup=kb.reply_lk)

			await state.reset_state()
			await Lk.choice.set()

# хэндлер получение от пользователя Save.app
@dp.message_handler(state=Save.app)
async def app(message: types.Message, state: FSMContext):
	app = message.text
	async with state.proxy() as data:
		data['app_request'] = app
		answer = data['app_request']
		try:
			if answer == '⬅️ Назад':
				await message.answer('Выбери тип, откуда ты хочешь отправить ссылку и придерживайся инструкции!',
					reply_markup=kb.reply_device)
				await state.reset_state()
			else:
				try:
					long_url = answer.split('&t=')[0]
					url = long_url.split('?v=')[1] # если всё ОК то получили id с привязкой ко времени сайт
				except IndexError:
					try:
						url = answer.split('?v=')[1] # если всё ОК то получили id с сайта
					except IndexError:
						try:
							long_url = answer.split('?t=')[0]
							url = long_url.split('/')[3] # если всё ОК то получили id с привязкой ко времени приложение
						except IndexError:
							try:
								url = long_url.split('/')[3] # если всё ОК то получили id из приложения
							except IndexError:
								await message.answer('Ты вводишь какую-то неправильную ссылку, отправь её мне снова, или вернись в Назад',
									reply_markup=kb.reply_back)

				await message.answer(url)
				await state.reset_state()
		except IndexError:
			await message.answer('Ты вводишь какую-то неправильную ссылку, отправь её мне снова, или вернись в Назад',
				reply_markup=kb.reply_back)

@dp.callback_query_handler(lambda message: message.data.startswith("fla_check"))
async def fla_check(callback_query: types.CallbackQuery, state:FSMContext):
	user_channel = await bot.get_chat_member(chat_id=-1001196469736, user_id=callback_query.from_user.id)
	if user_channel["status"] == 'left':
		"""для тех кто не подписался"""
		async with state.proxy() as data:
				fla = '0'
				data["crystal_fla"] = fla
		await bot.send_message(callback_query.from_user.id, 'Я проверил, ты не подписался. Подпишись чтобы получить кристаллы 😉',
			reply_markup=kb.reply_back)
	else:
		"""для тех кто подписался"""
		async with state.proxy() as data:
				fla = '100'
				data["crystal_fla"] = fla
		await bot.send_message(callback_query.from_user.id, 'Я проверил, ты подписался. Уже начислил тебе 100 кристаллов!\n\n'
			'Если отпишешься от канала, ты потеряешь все заработанные 💎. Нажимай Назад, чтобы вернуться в Личный кабинет',
			reply_markup=kb.reply_back)


@dp.callback_query_handler(lambda message: message.data.startswith("sell"))
async def sell(callback_query: types.CallbackQuery, state:FSMContext):
	await bot.send_message(callback_query.from_user.id, 'Недостаточно 💎 для действия. Обмен возможет только от 199, в скором времени у нас расширится база каналов и ты получишь еще больше кристаллов\n\n'
		'Если отпишешься от канала, ты потеряешь все заработанные 💎. Нажимай Назад, чтобы вернуться в Личный кабинет',
		reply_markup=kb.reply_back)