import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler
import sys
from dotenv import dotenv_values
sys.path.append("./src/scrap_diputades/src")
from full_scrapper import get_votaciones_by_name

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def bulid_vote_msg(vote):
    return str(vote)


async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    logging.info(f'/start from: {update.effective_chat.id}')
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!")


async def voto(update: Update, context: CallbackContext.DEFAULT_TYPE):
    logging.info(f'/vote from: {update.effective_chat.id}')
    name = update.message.text.split(' ')[1]
    logging.info(f'/vote expecting: {name}, scrapping votos')
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'paciencia, {name}')
    votos = get_votaciones_by_name(name)
    logging.info(f'/vote votos: {votos}')
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=votos)
    return

if __name__ == '__main__':
    config = dotenv_values(".env")
    if not config:
        config['TOKEN'] = os.getenv('TOKEN')
        config['HEROKU_APP_NAME'] = os.getenv('HEROKU_APP_NAME')
        config['PORT'] = os.getenv('PORT', default='8443')

    application = ApplicationBuilder().token(config['TOKEN']).build()
    start_handler = CommandHandler('start', start)
    voto = CommandHandler('voto', voto)
    application.add_handler(start_handler)
    application.add_handler(voto)
    application.run_polling()
    application.run_webhook(
        listen="0.0.0.0",
        port=int(config['PORT']),
        url_path=config['TOKEN'],
        webhook_url=f"https://{config['HEROKU_APP_NAME']}.herokuapp.com/"
                    + config['TOKEN']
        )

    # )
    # )
    # updater.start_webhook(
    #     listen="0.0.0.0",
    #                   port=int(os.environ.get('PORT', 5000)),
    #                   url_path=telegram_bot_token,
    #                   webhook_url=  + telegram_bot_token
    #                   )
    # 
