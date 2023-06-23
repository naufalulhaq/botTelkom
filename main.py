import logging
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler
from cred import token
import funcs

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

conversation_state = {}

def main():
    application = ApplicationBuilder().token(token).build()
    
    start_handler = CommandHandler('start', funcs.start_func)
    mulai_handler = CommandHandler('mulai', funcs.mulai_func)
    jenis_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), funcs.jenis_func)

    application.add_handler(start_handler)
    application.add_handler(mulai_handler)
    application.add_handler(jenis_handler)    

    application.run_polling()

if __name__ == '__main__':
    main()