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
# from config import TOKEN
# from telegram import InlineQueryResultPhoto, Update, InlineQueryResultArticle, InputTextMessageContent
# from telegram.ext import Application, ContextTypes, InlineQueryHandler
#
#
# async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     query = update.inline_query.query
#
#     if not query:
#         return
#
#     results = [
#         InlineQueryResultPhoto(
#             id=str(uuid4()),
#             photo_url="https://docs.python-telegram-bot.org/en/stable/_static/ptb-logo_1024.png",
#             thumbnail_url="https://docs.python-telegram-bot.org/en/stable/_static/ptb-logo_1024.png",),
#         InlineQueryResultArticle(id= str(uuid4()),title="BOT",url="https://docs.python-telegram-bot.org/en/stable/",input_message_content=InputTextMessageContent("Bot"))
#     ]
#
#     await update.inline_query.answer(results)
#
#
# def main() -> None:
#     application = Application.builder().token(TOKEN).build()
#     application.add_handler(InlineQueryHandler(inline_query))
#     application.run_polling()
#
#
# if __name__ == '__main__':
#     main()


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


# 9

# from telegram import Update, MessageEntity, ChatPermissions
# from telegram.ext import ContextTypes, Application, MessageHandler, filters, CallbackContext, Updater
# from config import TOKEN
# from datetime import datetime,timedelta
#
# user_delete_count = dict()
#
# async def user_restriction(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     user_restriction_time = datetime.now()+ timedelta(minutes=1)
#     user_id = update.message.from_user.id
#
#     try :
#         user_delete_count [user_id] += 1
#     except  KeyError:
#         user_delete_count[user_id] = 1
#
#     if user_delete_count[user_id] > 5:
#         await context.bot.restrict_chat_member(chat_id=update.message.chat.id, user_id=user_id,
#                                               permissions=ChatPermissions(can_send_messages=False ), until_date=user_restriction_time)
#
#     await context.bot.send_message(chat_id=update.message.chat.id, text=f"{update.message.from_user.first_name} you cant send links in this group.... !")
#
# async def delete_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     link_entity = [MessageEntity.URL]
#
#     if update.message.chat.type == ' supergroup':
#         if update.message.parse_entities(link_entity) or update.message.parse_caption_entity(types=link_entity):
#             await context.bot.delete_message(chat_id=update.message.chat.id, message_id=update.message.message_id)
#             await user_restriction(update, context)
#
#
# def main():
#     application = Application.builder().token(TOKEN).build()
#     application.add_handler(MessageHandler(filters.ALL, delete_message))
#     application.run_polling()
#
#     if __name__ == '__main__':
#       main()



# # 10
# import html
# import json
# from pickle import FALSE
# from pyexpat.errors import messages
# from config import TOKEN
# from telegram import Update
# from telegram.constants import ParseMode
# from telegram.ext import Application, CommandHandler, ContextTypes, Updater, CallbackContext
#
# DEVELOPER_CHAT_ID = 215053747
#
#
# async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE)-> None:
#     tb_list = [str(context.error), str(context.error.__traceback__)]
#     tb_string = ''.join(tb_list)
#
#     update_str = update.to_dict() if isinstance(update, Update) else str(update)
#     message = (
#         "An exception was raised while handing an updaete \n"
#         f"<pre>update = {html.escape(json.dumps(update_str, indent=2, ensure_ascii=False))}</pre>\n\n"
#         f"<pre>context.chat_date= {html.escape(str(context.chat_data))}</pre>\n\n"
#         f"<pre>context.user_data= {html.escape(str(context.user_data))}</pre>\n\n"
#         f"<pre>{html.escape(tb_string)}</pre>"
#     )
#
#
#     await context.bot.send_message(chat_id=DEVELOPER_CHAT_ID, text=message, parse_mode=ParseMode.HTML)
#
#
#
#
# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE ) -> None:
#     await context.bot.bad_method_name()
#
# def main() -> None:
#    application = Application.builder().token(TOKEN).build()
#    application.add_handler(CommandHandler('help', help_command))
#    application.add_error_handler(error_handler)
#    application.run_polling(allowed_updates=Update.ALL_TYPES)
#
#
# if __name__ == '__main__':
#     main()


# 11
from config import TOKEN
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, Application, ContextTypes, CallbackQueryHandler, CallbackContext, Updater

BOT2_CHANNEL= "@bott2za"
MAIN_CHANNEL_LINK = "https://t.me/SmartyPaantsBott"

async def is_member(bot, channel, user_id):
    try:
      member = await bot.get_chat_member(channel, user_id)
      return member.status in ("member", "administrator", "creator")
    except:
       return False


async def start (update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if await is_member(context.bot, BOT2_CHANNEL, user_id):
        keyword = [InlineKeyboardButton("enter main channel ", url=MAIN_CHANNEL_LINK)]
        await update.message.reply_text("Your subcription approved", reply_markup=InlineKeyboardMarkup(keyword))
    else:
        keyword = [
            [InlineKeyboardButton(
                "You must subscribe in required channel",
                url=f"https://t.me/{BOT2_CHANNEL.replace('@', '')}"
            )],
            [InlineKeyboardButton(
                "Check subscription",
                callback_data="subscribe"
            )]
        ]
    await update.message.reply_text("You must subscribe in required channel first",
                                    reply_markup=InlineKeyboardMarkup(keyword))


async def check_membership (update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if await is_member(context.bot, BOT2_CHANNEL, user_id):
        await query.edit_message_text(f"Your subscription approved \n\n, main channel link\n\n{MAIN_CHANNEL_LINK}")
    else:
        await context.bot.send_message(update.effective_chat.id, f"You must subscribe in required channel first")


def main():
    app= Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check_membership, pattern="subscribe"))
    app.run_polling(allowed_updates=Update.ALL_TYPES)



if __name__ == '__main__':
    main()



