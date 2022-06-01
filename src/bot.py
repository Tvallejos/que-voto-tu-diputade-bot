import logging
from telegram.ext import ApplicationBuilder
from settings import set_config, add_handlers, declare_handlers

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler("diputade.log", mode='a'),
        logging.StreamHandler()
    ]
)

if __name__ == '__main__':
    config = set_config()
    application = ApplicationBuilder().token(config['TOKEN']).build()
    add_handlers(application, declare_handlers())
    application.run_polling()
