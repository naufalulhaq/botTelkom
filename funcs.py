
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

FIRST_QUESTION, JENIS_WARUNG, JENIS_MINIMARKET, JENIS_BENGKEL, JENIS_DEALER, JENIS_BARBER, JENIS_FASHION, JENIS_LAUNDRY, JENIS_GADGET, WARUNG_1, WARUNG_2 = range(11)

async def start_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Hi! Selamat datang di Telkom SDA SME IS Bot. Temukan solusi untuk Usaha miliki anda sekarang juga!\n\nklik /mulai untuk memulai!")


async def mulai_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
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

    await update.message.reply_text(question)
    return FIRST_QUESTION

async def jenis_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 9:
            if number == 1:
                question = "Jenis usaha anda adalah warung. Dalam skala manakah anda menggambarkan usaha anda?\n" \
               "1. Skala small (omzet 300 Juta - 2,5 Miliar / tahun)\n" \
               "2. Skala micro (omzet 300 Juta/ tahun)"
                await update.message.reply_text(question)
                return JENIS_WARUNG
            elif number == 2:
                uestion = "...?\n" \
               "1. ...\n" \
               "2. ..."
                await update.message.reply_text(question)
                return JENIS_MINIMARKET
            # Tambahkan kondisi untuk pilihan2
            else:
                await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
    return ConversationHandler.END

async def jenis_warung_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 2:
            if number == 1:
                question = "Usaha warung anda berskala small (omzet 300 Juta - 2,5 Miliar / tahun). Apa keluhan usaha anda?\n" \
                   "1. Membutuhkan internet untuk operasional toko \n" \
                   "2. Membutuhkan sistem keamanan lokasi di seluruh cabang \n" \
                   "3. Ingin memiliki metode pembayaran yang universal melalui QRIS generator \n" \
                   "4. Membutuhkan sistem POS yang dapat menampung SKU lebih banyak"
                await update.message.reply_text(question)
                return WARUNG_1
            elif number == 2:
                question = "Usaha warung anda berskala micro (omzet 300 Juta/ tahun). Apa keluhan usaha anda?\n" \
                   "1. Membutuhkan internet untuk operasional toko \n" \
                   "2. Ingin memiliki metode pembayaran yang universal melalui QRIS generator \n" \
                   "3. Membutuhkan sistem kasir sederhana untuk pencatatan transaksi dan monitoring stock"
                await update.message.reply_text(question)
                return WARUNG_2
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
    return ConversationHandler.END

async def warung_1_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 4:
            await update.message.reply_text("Usaha anda berskala small (omzet 300 Juta - 2,5 Miliar / tahun)")
            return WARUNG_1
        else:
            await update.message.reply_text("Usaha anda berskala micro (omzet 300 Juta/ tahun)")
            return WARUNG_2
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
    return ConversationHandler.END