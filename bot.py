import os
import json
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# from utils.viotp import Viotp
from message_template import messageXSMB

from handlers.command_handers import xs


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def add_user(update, context):
    user = update.effective_user
    await update.message.reply_text(f'''
                                    {user.get_profile_photos}
                                    ''')


async def add_key(update, context):
    key = None





def main():
    bot_token = os.getenv("BOT_API")
    if not bot_token:
        print("Bot token is not set. Please set the BOT_API environment variable.")
        return

    application = ApplicationBuilder().token(
        bot_token).concurrent_updates(True).build()
    application.add_handler(CommandHandler("hello", hello))
    application.add_handler(CommandHandler("add_user", add_user))
    application.add_handler(CommandHandler("xs", xs))

    print("Bot is running...")
    application.run_polling()


if __name__ == '__main__':
    main()
