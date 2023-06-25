import logging
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ConversationHandler
from cred import token
from functions import *
from states import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    application = ApplicationBuilder().token(token).build()
    
    start_handler = CommandHandler('start', start_func)
    jenis_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), jenis_func)

    main_handler = ConversationHandler(
        entry_points=[CommandHandler('mulai', mulai_func)],
        states={
            FIRST_QUESTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, jenis_func)],
            JENIS_WARUNG: [MessageHandler(filters.TEXT & ~filters.COMMAND, jenis_warung_func)],
            # JENIS_MINIMARKET: [MessageHandler(filters.TEXT & ~filters.COMMAND, jenis_minimarket_func)],
            # JENIS_BENGKEL: [MessageHandler(filters.TEXT & ~filters.COMMAND, jenis_bengkel_func)],
            # JENIS_DEALER: [MessageHandler(filters.TEXT & ~filters.COMMAND, jenis_dealer_func)],
            # JENIS_BARBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, jenis_barber_func)],
            # JENIS_FASHION: [MessageHandler(filters.TEXT & ~filters.COMMAND, jenis_fashion_func)],
            # JENIS_LAUNDRY: [MessageHandler(filters.TEXT & ~filters.COMMAND, jenis_laundry_func)],
            # JENIS_GADGET: [MessageHandler(filters.TEXT & ~filters.COMMAND, jenis_gadget_func)],
            WARUNG_1: [MessageHandler(filters.TEXT & ~filters.COMMAND, warung_1_func)],
            # WARUNG_2: [MessageHandler(filters.TEXT & ~filters.COMMAND, warung_2_func)],
            # Add states and handlers for other second questions here
        },
        fallbacks=[start_handler]
    )

    application.add_handler(start_handler)
    application.add_handler(main_handler)
    application.add_handler(jenis_handler)    

    application.run_polling()

if __name__ == '__main__':
    main()