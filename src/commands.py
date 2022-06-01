import logging
from telegram import Update
from telegram.ext import CallbackContext
import sys
from message import string_of_vote
sys.path.append("./src/scrap_diputades/src")
#sys.path.append("./scrap_diputades/src")
from full_scrapper import get_votaciones_by_name
import exceptions as e


async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    logging.info(f'/start from: {update.effective_chat.id}')
    text = "Hola! Soy un bot en fase beta, tenme paciencia unu. \n"
    text += "Puedes buscar el último voto de tu diputade con el comando"
    text += " /voto nombre"
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=text)


async def voto(update: Update, context: CallbackContext.DEFAULT_TYPE):
    logging.info(f'call from: {update.effective_chat.id}')
    name = update.message.text.split(' ')[1]
    logging.info(f'/vote expecting: {name}, scrapping votos')
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'paciencia, {name}')
    try:
        votos = string_of_vote(get_votaciones_by_name(name), False)
    except (e.DiputadeNotFound, e.MultiplesDiputadesFound) as exp:
        votos = exp.message

    logging.info(f'/vote votos: {votos}')
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=votos,
        parse_mode='HTML')
    return
