
from telegram import Update
from telegram.ext import ContextTypes

conversation_state = {}

async def start_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Hi! Selamat datang di Telkom SDA SME IS Bot. Temukan solusi untuk Usaha miliki anda sekarang juga!\n\nklik /mulai untuk memulai!")

async def mulai_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id=update.effective_chat.id
    question = "Apa jenis usaha kamu?\n" \
               "1. Warung/ Toko Kelontong\n" \
               "2. Minimarket\n" \
               "3. Pujasera\n" \
               "4. Automotive (Bengkel)\n" \
               "5. Automotive (Dealer)\n" \
               "6. Barbershop/ Salon\n" \
               "7. Fashion/ Boutique\n" \
               "8. Laundry\n" \
               "9. Gadget & Elektronik"

    await context.bot.send_message(chat_id=user_id, text=question)
    conversation_state[user_id] = 'awaiting_answer'

async def jenis_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id

    if user_id in conversation_state and conversation_state[user_id] == 'awaiting_answer':
        answer = update.message.text.strip()
        if answer.isdigit():
            number = int(answer)
            if number >= 1 and number <= 4:
                if number == 1:
                    response = "Your favorite color is Red."
                elif number == 2:
                    response = "Your favorite color is Blue."
                elif number == 3:
                    response = "Your favorite color is Green."
                elif number == 4:
                    response = "Your favorite color is Yellow."
            else:
                response = "Invalid answer. Please choose a number from 1 to 4."
        else:
            response = "Invalid answer. Please provide a number."

        await context.bot.send_message(chat_id=user_id, text=response)

        # Clear the conversation state after the answer has been processed
        del conversation_state[user_id]
    else:
        start_func()