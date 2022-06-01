import os
from dotenv import dotenv_values
from commands import start, voto
from telegram.ext import CommandHandler, Application
from typing import List


def set_config():
    config = dotenv_values(".env")
    if not config:
        config['TOKEN'] = os.getenv('TOKEN')
        config['HEROKU_APP_NAME'] = os.getenv('HEROKU_APP_NAME')
        config['PORT'] = os.getenv('PORT', default='8443')
    return config


def declare_handlers() -> List[CommandHandler]:
    handlers = []
    handlers.append(CommandHandler('start', start))
    handlers.append(CommandHandler('voto', voto))
    return handlers


def add_handlers(application: Application, handlers: List[CommandHandler]):
    for h in handlers:
        application.add_handler(h)
    return
