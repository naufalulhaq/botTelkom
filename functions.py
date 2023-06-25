
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from states import *

async def start_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Hi! Selamat datang di Telkom SDA SME IS Bot. Temukan solusi untuk Usaha miliki anda sekarang juga!\n\nklik /mulai untuk memulai!")


async def mulai_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = "Apa jenis usaha Anda?\n\n" \
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
                question = "Jenis usaha anda adalah minimarket. Apa keluhan usaha anda?\n" \
               "1. Membutuhkan internet (ber IP static) yang lebih stabil untuk operasional toko yang dapat dimonitor di beberapa cabang\n" \
               "2. Membutuhkan sistem pembayaran yang lebih advance dengan fitur payment gateway, BI RTGS, Transfer dana, Uang elektronik, Debit acquirer, Quick Respon (QR) Code, Wallet)\n" \
               "3. Membutuhkan cloud untuk penyimpanan data\n" \
               "4. Membutuhkan sistem distribusi (yang dikelola toko sendiri)\n" \
               "5. Membutuhkan sistem keamanan lokasi di seluruh cabang\n" \
               "6. Ingin memiliki metode pembayaran yang universal melalui QRIS generator\n" \
               "7. Membutuhkan sistem POS yang dapat menampung SKU lebih banyak\n" \
               "8. Membutuhkan WA blast untuk menginfokan promo ke para pelanggannya"
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

# WARUNG
async def jenis_warung_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 2:
            if number == 1:
                question = "Usaha warung anda berskala small (omzet 300 Juta - 2,5 Miliar / tahun). Apa keluhan usaha anda?\n\n" \
                   "1. Membutuhkan internet untuk operasional toko \n" \
                   "2. Membutuhkan sistem keamanan lokasi di seluruh cabang \n" \
                   "3. Ingin memiliki metode pembayaran yang universal melalui QRIS generator \n" \
                   "4. Membutuhkan sistem POS yang dapat menampung SKU lebih banyak"
                await update.message.reply_text(question)
                return WARUNG_1
            elif number == 2:
                question = "Usaha warung anda berskala micro (omzet 300 Juta/ tahun). Apa keluhan usaha anda?\n\n" \
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
            if number == 1:
                await solution_hsi(update=update, context=context)
                return END_QUESTION
            elif number == 2:
                await solution_indibiz_cam(update=update, context=context)
                return END_QUESTION
            elif number == 3:
                await solution_indibiz_pay(update=update, context=context)
                return END_QUESTION
            elif number == 4:
                await solution_indibiz_kasir(update=update, context=context)
                return END_QUESTION
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return END_QUESTION
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
    return ConversationHandler.END

async def warung_2_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 3:
            if number == 1:
                await solution_hsi(update=update, context=context)
                return END_QUESTION
            elif number == 2:
                await solution_indibiz_pay(update=update, context=context)
                return END_QUESTION
            elif number == 3:
                await solution_indibiz_pay(update=update, context=context)
                return END_QUESTION
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return END_QUESTION
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
    return ConversationHandler.END

# MINIMARKET
async def jenis_warung_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 8:
            if number == 1:
                await solution_astinet(update, context)
                return END_QUESTION
            elif number == 2:
                await solution_finpay( update, context)
                return END_QUESTION
            elif number == 2:
                await solution_flou( update, context)
                return END_QUESTION
            elif number == 3:
                await solution_dms( update, context)
                return END_QUESTION
            elif number == 4:
                await solution_indibiz_cam( update, context)
                return END_QUESTION
            elif number == 5:
                await solution_indibiz_pay( update, context)
                return END_QUESTION
            elif number == 6:
                await solution_indibiz_kasir( update, context)
                return END_QUESTION
            elif number == 7:
                await solution_oca( update, context)
                return END_QUESTION
            elif number == 8:
                await solution_finpay( update, context)
                return END_QUESTION
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
    return ConversationHandler.END

# PUJASERA
# BENGKEL
# DEALER
# BARBER
# FASHION
# LAUNDRY
# GADGET

## SOLUTIONS
# DIGITAL CONNECTIVITY
async def solution_hsi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk HSI/Indibiz\n" \
            "HSI adalah ..."
    await context.bot.send_message(chat_id=user_id, text=text)

async def solution_astinet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk Astinet\n" \
            "Astinet adalah ..."
    await context.bot.send_message(chat_id=user_id, text=text)

async def solution_netmonk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk Netmonk\n" \
            "Netmonk adalah ..."
    await context.bot.send_message(chat_id=user_id, text=text)

async def solution_wms(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk WMS/Indibiz Wifi\n" \
            "WMS adalah ..."
    await context.bot.send_message(chat_id=user_id, text=text)

async def solution_metro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk Metro E\n" \
            "Metro E adalah ..."
    await context.bot.send_message(chat_id=user_id, text=text)

# DIGITAL PLATFORM
async def solution_finpay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk Finpay\n" \
            "Finpay adalah ..."
    await context.bot.send_message(chat_id=user_id, text=text)

async def solution_flou(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk Flou\n" \
            "Flou adalah ..."
    await context.bot.send_message(chat_id=user_id, text=text)

async def solution_erp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk ERP\n" \
            "ERP adalah ..."
    await context.bot.send_message(chat_id=user_id, text=text)

async def solution_dms(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk DMS\n" \
            "DMS adalah ..."
    await context.bot.send_message(chat_id=user_id, text=text)

# DIGITAL SERVICE
async def solution_indibiz_cam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk Indibiz Cam\n" \
            "Indibiz Cam adalah ..."
    await context.bot.send_message(chat_id=user_id, text=text)

async def solution_indibiz_pay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk Indibiz Pay\n" \
            "Indibiz Pay adalah ..."
    await context.bot.send_message(chat_id=user_id, text=text)

async def solution_indibiz_kasir(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk Indibiz Kasir\n" \
            "Indibiz Kasir adalah ..."
    await context.bot.send_message(chat_id=user_id, text=text)

async def solution_oca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk OCA\n" \
            "OCA adalah ..."
    await context.bot.send_message(chat_id=user_id, text=text)