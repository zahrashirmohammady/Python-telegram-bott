#
# from telegram.ext import ContextTypes, Application, CallbackContext, CommandHandler
# from telegram import Update
# from config import TOKEN
#
#
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text("hi !use/ set <second> to set a timer")
#
# async def alarm(context:ContextTypes.DEFAULT_TYPE) -> None:
#     job = context.job
#     await context.bot.send_message(job.chat_id, text=f"Beep! {job.data} seconds are over!")
#
#
# def remove_job_if_exists(name, context: ContextTypes.DEFAULT_TYPE) -> None:
#   current_jobs = context.job_queue.get_jobs_by_name(name)
#   if not current_jobs:
#       return float
#   for job in current_jobs:
#       job.schedule_removal()
#   return True
#
#
# async def set_timer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     chat_id = update.effective_message.chat_id
#     try:
#       due = float(context.args[0])
#       if due < 0:
#           await  update.effective_message.reply_text("Sorry, we cant go back to future!")
#           return
#
#       job_removed = remove_job_if_exists(str(chat_id), context)
#       context.job_queue.run_once(alarm, due, chat_id=chat_id, name=str(chat_id), data=due)
#
#       text = "Timer successfully set!"
#       if job_removed:
#          text += "and old one was removed."
#       await update.effective_message.reply_text("Usage:/ set<seconds>")
#
#     except (IndexError, ValueError):
#       await update.effective_message.reply_text("Usage:/ set<seconds>")
#
# async def unset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     chat_id = update.message.chat_id
#     job_removed = remove_job_if_exists(str(chat_id), context)
#     text = "Timer successfully cancelled!" if job_removed else "You have no active timer."
#     await update.effective_message.reply_text(text)
#
#
#
# def main():
#     application = Application.builder().token(TOKEN).build()
#
#     application.add_handler(CommandHandler(['start', 'help'], start))
#     application.add_handler(CommandHandler("unset", unset))
#     application.run_polling(allowed_updates=Update.ALL_TYPES)
#
# if __name__ == '__main__':
#     main()



# 7
#
# from uuid import uuid4
from config import TOKEN
from telegram import InlineQueryResultPhoto, Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Application, ContextTypes, InlineQueryHandler


async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.inline_query.query

    if not query:
        return

    results = [
        InlineQueryResultPhoto(
            id=str(uuid4()),
            photo_url="https://docs.python-telegram-bot.org/en/stable/_static/ptb-logo_1024.png",
            thumbnail_url="https://docs.python-telegram-bot.org/en/stable/_static/ptb-logo_1024.png",),
        InlineQueryResultArticle(id= str(uuid4()),title="BOT",url="https://docs.python-telegram-bot.org/en/stable/",input_message_content=InputTextMessageContent("Bot"))
    ]

    await update.inline_query.answer(results)


def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(InlineQueryHandler(inline_query))
    application.run_polling()


if __name__ == '__main__':
    main()


#
# from telegram import Update, MessageEntity
# from telegram.ext import ContextTypes, Application, MessageHandler, filters
# from config import TOKEN
#
#
# async def delete_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     if not update.message:
#         return
#
#     if update.message.chat.type in ["group", "supergroup"]:
#
#         entities = update.message.parse_entities([MessageEntity.URL])
#
#         if entities:
#             await update.message.delete()
#
#
# def main():
#     application = Application.builder().token(TOKEN).build()
#     application.add_handler(MessageHandler(filters.ALL, delete_message))
#     application.run_polling()
#
#
# if __name__ == '__main__':
#     main()
