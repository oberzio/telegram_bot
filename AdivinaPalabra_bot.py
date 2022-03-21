# -*- coding: utf-8 -*-
'''
Bot para telegram
'''
import random
from turtle import update
from telegram import (ParseMode)
from telegram.ext import (Updater, CommandHandler)

# [Opcional] Recomendable poner un log con los errores que apareceran por pantalla.
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)
def error_callback(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def start(update, context):
	''' START '''
	# Enviar un mensaje a un ID determinado.
	context.bot.send_message(update.message.chat_id, "Bienvenido", parse_mode=ParseMode.HTML)

	# Podemos llamar a otros comandos, sin que se haya activado en el chat (/help).
	wordex(update, context)

def wordex(update, context):
	cid=update.message.chat_id
    username=update.message.chat['first_name']
	msg = "Hola " + username
	# Responde directametne en el canal donde se le ha hablado.
	update.message.reply_text(msg)

def main():
	TOKEN="5140146266:AAGt9Uuk9vXM6UM7tGzkhbMdMpbAiOpzr9o"
	updater=Updater(TOKEN, use_context=True)
	dp=updater.dispatcher

	# Eventos que activarán nuestro bot.
	# /comandos
	dp.add_handler(CommandHandler('start',	start))
	dp.add_handler(CommandHandler('play',	wordex))

	dp.add_error_handler(error_callback)
    # Comienza el bot
	updater.start_polling()
    # Lo deja a la escucha. Evita que se detenga.
	updater.idle()

if __name__ == '__main__':
	print(('[Nombre del bot] Start...'))
	main()
