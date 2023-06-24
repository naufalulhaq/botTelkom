from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler
import funcConvo as fu
from cred import token
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Define conversation states
FIRST_QUESTION = range(1)
SECOND_QUESTION_A, SECOND_QUESTION_B, SECOND_QUESTION_C, SECOND_QUESTION_D, SECOND_QUESTION_E, SECOND_QUESTION_F = range(6)


def main():
    application = ApplicationBuilder().token(token).build()

    # Add handlers
    start_handler = CommandHandler('start', fu.start_func)
    main_handler = ConversationHandler(
        entry_points=[CommandHandler('mulai', fu.mulai)],
        states={
            FIRST_QUESTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, fu.first_question)],
            SECOND_QUESTION_A: [MessageHandler(filters.TEXT & ~filters.COMMAND, fu.second_question_a)],
            SECOND_QUESTION_D: [MessageHandler(filters.TEXT & ~filters.COMMAND, fu.second_question_d)],
            # Add states and handlers for other second questions here
        },
        fallbacks=[MessageHandler(filters.TEXT, fu.start)]
    )

    application.add_handler(main_handler)

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
