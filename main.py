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
    # exit_handler = CommandHandler('end', exitt)
    main_handler = ConversationHandler(
        entry_points=[CommandHandler('mulai', mulai_func)],
        states={
            FIRST_QUESTION: [MessageHandler(filters.TEXT & ~filters.COMMAND, jenis_func)],
            
            JENIS_WARUNG: [MessageHandler(filters.TEXT & ~filters.COMMAND, jenis_warung_func)],
            JENIS_MINIMARKET: [MessageHandler(filters.TEXT & ~filters.COMMAND, jenis_minimarket_func)],
            JENIS_PUJASERA: [MessageHandler(filters.TEXT & ~filters.COMMAND, jenis_pujasera_func)],
            JENIS_BENGKEL: [MessageHandler(filters.TEXT & ~filters.COMMAND, jenis_bengkel_func)],
            JENIS_DEALER: [MessageHandler(filters.TEXT & ~filters.COMMAND, jenis_dealer_func)],
            JENIS_BARBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, jenis_barber_func)],
            JENIS_FASHION: [MessageHandler(filters.TEXT & ~filters.COMMAND, jenis_fashion_func)],
            JENIS_LAUNDRY: [MessageHandler(filters.TEXT & ~filters.COMMAND, jenis_laundry_func)],
            JENIS_GADGET: [MessageHandler(filters.TEXT & ~filters.COMMAND, jenis_gadget_func)],

            WARUNG_1: [MessageHandler(filters.TEXT & ~filters.COMMAND, warung_1_func)],
            WARUNG_2: [MessageHandler(filters.TEXT & ~filters.COMMAND, warung_2_func)],
            PUJASERA_1: [MessageHandler(filters.TEXT & ~filters.COMMAND, pujasera_1_func)],
            PUJASERA_2: [MessageHandler(filters.TEXT & ~filters.COMMAND, pujasera_2_func)],
            BENGKEL_1: [MessageHandler(filters.TEXT & ~filters.COMMAND, bengkel_1_func)],
            BENGKEL_2: [MessageHandler(filters.TEXT & ~filters.COMMAND, bengkel_2_func)],
            BARBER_1: [MessageHandler(filters.TEXT & ~filters.COMMAND, barber_1_func)],
            BARBER_2: [MessageHandler(filters.TEXT & ~filters.COMMAND, barber_2_func)],
            FASHION_1: [MessageHandler(filters.TEXT & ~filters.COMMAND, fashion_1_func)],
            FASHION_2: [MessageHandler(filters.TEXT & ~filters.COMMAND, fashion_2_func)],
            LAUNDRY_1: [MessageHandler(filters.TEXT & ~filters.COMMAND, laundry_1_func)],
            LAUNDRY_2: [MessageHandler(filters.TEXT & ~filters.COMMAND, laundry_2_func)],
            GADGET_1: [MessageHandler(filters.TEXT & ~filters.COMMAND, gadget_1_func)],
            GADGET_2: [MessageHandler(filters.TEXT & ~filters.COMMAND, gadget_2_func)],
        },
        fallbacks=[start_handler]
    )

    application.add_handler(start_handler)
    application.add_handler(main_handler)
    # application.add_handler(exit_handler)    

    application.run_polling()

if __name__ == '__main__':
    main()