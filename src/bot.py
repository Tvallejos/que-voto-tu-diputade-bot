import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler
import sys
sys.path.append("./src/scrap_diputades")
from scrap_diputades.full_scrapper import get_votaciones_by_name
from dotenv import dotenv_values
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def bulid_vote_msg(vote):
    return str(vote)

async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    logging.info(f'/start from: {update.effective_chat.id}')
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def voto(update: Update, context: CallbackContext.DEFAULT_TYPE):
    logging.info(f'/vote from: {update.effective_chat.id}')
    name = update.message.text.split(' ')[1]
    logging.info(f'/vote expecting: {name}, scrapping votos')
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'paciencia, {name}')
    votos = get_votaciones_by_name(name)
    logging.info(f'/vote votos: {votos}')
    await context.bot.send_message(chat_id=update.effective_chat.id, text=votos)
    return

if __name__ == '__main__':
    config = dotenv_values(".env") 
    application = ApplicationBuilder().token(config['TOKEN']).build()
    
    start_handler = CommandHandler('start', start)
    voto = CommandHandler('voto', voto)
    application.add_handler(start_handler)
    application.add_handler(voto)
    
    application.run_polling()
