import logging

from telegram.ext import (ApplicationBuilder, CommandHandler, MessageHandler,
                          filters)

from config.settings import Settings
from handlers import get_all_data, register, start, unknown


def main():
    logging.info("Starting")
    application = ApplicationBuilder().token(Settings.BOT_TOKEN).build()

    logging.info("Instancing handlers")
    start_handler = CommandHandler('start', start)
    register_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), register)
    get_sheet_data_handler = CommandHandler('mostrar', get_all_data)
    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    logging.info("Registering handlers")
    application.add_handler(start_handler)
    application.add_handler(register_handler)
    application.add_handler(get_sheet_data_handler)
    application.add_handler(unknown_handler)

    logging.info("Listening")
    application.run_polling()


if __name__ == '__main__':
    main()
