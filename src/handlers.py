from telegram import Update
from telegram.ext import ContextTypes

from actions import Actions

Context = ContextTypes.DEFAULT_TYPE

async def start(update: Update, context: Context):
    uname = update.effective_user.first_name
    message = f"Opa! E aí {uname}?"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

async def register(update: Update, context: Context):
    response = await Actions.register_run(update.message.text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def get_all_data(update: Update, context: Context):
    response = await Actions.get_entire_sheet_data()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def unknown(update: Update, context: Context):
    message = "Não entendi..."
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
