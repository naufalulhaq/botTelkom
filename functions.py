
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

async def jenis_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
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
                question = "Jenis usaha anda adalah minimarket. Apa keluhan usaha anda?\n\n" \
               "1. Membutuhkan internet (ber IP static) yang lebih stabil untuk operasional toko yang dapat dimonitor di beberapa cabang\n" \
               "2. Membutuhkan sistem pembayaran yang lebih advance dengan fitur payment gateway, BI RTGS, Transfer dana, Uang elektronik, Debit acquirer, Quick Respon (QR) Code, Wallet)\n" \
               "3. Membutuhkan cloud untuk penyimpanan data\n" \
               "4. Membutuhkan sistem distribusi (yang dikelola toko sendiri)\n" \
               "5. Membutuhkan sistem keamanan lokasi di seluruh cabang\n" \
               "6. Ingin memiliki metode pembayaran yang universal melalui QRIS generator\n" \
               "7. Membutuhkan sistem POS yang dapat menampung SKU lebih banyak\n" \
               "8. Membutuhkan WA blast untuk menginfokan promo ke para pelanggan"
                await update.message.reply_text(question)
                return JENIS_MINIMARKET
            elif number == 3:
                question = "Jenis usaha anda adalah pujasera. Mana yang di bawah ini yang menggambarkan usaha anda?\n\n" \
               "1. Service Dine In, tidak memiliki cabang\n" \
               "2. Service Take Away, tidak memiliki cabang"
                await update.message.reply_text(question)
                return JENIS_PUJASERA
            elif number == 4:
                question = "Jenis usaha anda adalah automotive (bengkel). Mana yang di bawah ini yang menggambarkan usaha anda?\n\n" \
               "1. Memiliki beberapa cabang\n" \
               "2. Tidak memiliki cabang"
                await update.message.reply_text(question)
                return JENIS_BENGKEL
            elif number == 5:
                question = "Jenis usaha anda adalah automotive (dealer). Apa keluhan usaha anda?\n\n" \
               "1. Membutuhkan jaringan internet yg lebih stabil\n" \
               "2. Membutuhkan solusi komunikasi berbasis ethernet untuk menghubungkan 2 titik atau lebih yang terpisah satu sama lain\n" \
               "3. Memiliki beberapa cabang yang membutuhkan monitoring untuk internet\n" \
               "4. Membutuhkan sistem pembayaran yang lebih advance (dengan fitur payment gateway, BI RTGS, Transfer dana, Uang elektronik, Debit acquirer, Quick Respon (QR) Code, Wallet) atau Ingin memiliki metode pembayaran yang universal melalui QRIS generator\n" \
               "5. Membutuhkan monitoring keamanan lokasi\n" \
               "6. Membutuhkan WA/ SMS blast untuk penawaran / promo"
                await update.message.reply_text(question)
                return JENIS_DEALER
            elif number == 6:
                question = "Jenis usaha anda adalah barbershop/salon. Mana yang di bawah ini yang menggambarkan usaha anda?\n\n" \
               "1. Memiliki beberapa cabang\n" \
               "2. Tidak memiliki cabang"
                await update.message.reply_text(question)
                return JENIS_BARBER
            elif number == 7:
                question = "Jenis usaha anda adalah fashion/boutique. Mana yang di bawah ini yang menggambarkan usaha anda?\n\n" \
               "1. Memiliki beberapa cabang\n" \
               "2. Tidak memiliki cabang"
                await update.message.reply_text(question)
                return JENIS_FASHION
            elif number == 8:
                question = "Jenis usaha anda adalah laundry. Mana yang di bawah ini yang menggambarkan usaha anda?\n\n" \
               "1. Memiliki beberapa cabang\n" \
               "2. Tidak memiliki cabang"
                await update.message.reply_text(question)
                return JENIS_LAUNDRY
            elif number == 9:
                question = "Jenis usaha anda adalah gadget & elektronik. Mana yang di bawah ini yang menggambarkan usaha anda?\n\n" \
               "1. Toko Gadget & Elektronik yang memiliki beberapa cabang\n" \
               "2. Counter HP/ Pulsa yang tidak memiliki cabang"
                await update.message.reply_text(question)
                return JENIS_GADGET
            # Tambahkan kondisi untuk pilihan2
            else:
                await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return FIRST_QUESTION
    elif user_answer.lower() == 'exit':
        await exit_func(update, context)
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return FIRST_QUESTION

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
            return JENIS_WARUNG
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return JENIS_WARUNG

async def warung_1_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 4:
            if number == 1:
                await solution_hsi(update=update, context=context)
                return ConversationHandler.END
            elif number == 2:
                await solution_indibiz_cam(update=update, context=context)
                return ConversationHandler.END
            elif number == 3:
                await solution_indibiz_pay(update=update, context=context)
                return ConversationHandler.END
            elif number == 4:
                await solution_indibiz_kasir(update=update, context=context)
                return ConversationHandler.END
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return WARUNG_1
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return WARUNG_1

async def warung_2_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 3:
            if number == 1:
                await solution_hsi(update=update, context=context)
                return ConversationHandler.END
            elif number == 2:
                await solution_indibiz_pay(update=update, context=context)
                return ConversationHandler.END
            elif number == 3:
                await solution_indibiz_pay(update=update, context=context)
                return ConversationHandler.END
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return WARUNG_2
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return WARUNG_2

# MINIMARKET
async def jenis_minimarket_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 8:
            if number == 1:
                await solution_astinet(update, context)
                return ConversationHandler.END
            elif number == 2:
                await solution_finpay( update, context)
                return ConversationHandler.END
            elif number == 3:
                await solution_flou( update, context)
                return ConversationHandler.END
            elif number == 4:
                await solution_dms( update, context)
                return ConversationHandler.END
            elif number == 5:
                await solution_indibiz_cam( update, context)
                return ConversationHandler.END
            elif number == 6:
                await solution_indibiz_pay( update, context)
                return ConversationHandler.END
            elif number == 7:
                await solution_indibiz_kasir( update, context)
                return ConversationHandler.END
            elif number == 8:
                await solution_oca( update, context)
                return ConversationHandler.END
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return JENIS_MINIMARKET
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return JENIS_MINIMARKET

# PUJASERA
async def jenis_pujasera_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 2:
            if number == 1:
                question = "Usaha pujasera anda menawarkan service dine in dan tidak memiliki cabang. Apa keluhan usaha anda?\n\n" \
                   "1. Membutuhkan internet untuk operasional toko dan wifi untuk keperluan pengunjung (bisa di provide oleh pemilik, bisa di jual melalui sistem voucher) \n" \
                   "2. Membutuhkan monitoring untuk menjaga keamanan lokasi \n" \
                   "3. Ingin memiliki metode pembayaran yang universal melalui QRIS generator \n" \
                   "4. Membutuhkan sistem kasir yang lebih advance (hingga ke fitur table management)"
                await update.message.reply_text(question)
                return PUJASERA_1
            elif number == 2:
                question = "Usaha pujasera anda menawarkan service take away dan tidak memiliki cabang. Apa keluhan usaha anda?\n\n" \
                   "1. Membutuhkan internet untuk operasional toko \n" \
                   "2. Membutuhkan monitoring untuk menjaga keamanan lokasi \n" \
                   "3. Ingin memiliki metode pembayaran yang universal melalui QRIS generator \n" \
                   "4. Membutuhkan sistem kasir untuk pencatatan transaksi, reporting, dll"
                await update.message.reply_text(question)
                return PUJASERA_2
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return JENIS_PUJASERA
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return JENIS_PUJASERA

async def pujasera_1_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 4:
            if number == 1:
                await solution_hsi(update=update, context=context)
                return ConversationHandler.END
            elif number == 2:
                await solution_indibiz_cam(update=update, context=context)
                return ConversationHandler.END
            elif number == 3:
                await solution_indibiz_pay(update=update, context=context)
                return ConversationHandler.END
            elif number == 4:
                await solution_indibiz_kasir(update=update, context=context)
                return ConversationHandler.END
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return PUJASERA_1
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return PUJASERA_1

async def pujasera_2_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 4:
            if number == 1:
                await solution_hsi(update=update, context=context)
                return ConversationHandler.END
            elif number == 2:
                await solution_indibiz_cam(update=update, context=context)
                return ConversationHandler.END
            elif number == 3:
                await solution_indibiz_pay(update=update, context=context)
                return ConversationHandler.END
            elif number == 4:
                await solution_indibiz_kasir(update=update, context=context)
                return ConversationHandler.END
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return PUJASERA_2
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return PUJASERA_2

# BENGKEL
async def jenis_bengkel_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 2:
            if number == 1:
                question = "Usaha automotive (bengkel) anda memiliki beberapa cabang. Apa keluhan usaha anda?\n\n" \
                   "1. Membutuhkan jaringan internet yg lebih stabil\n" \
                   "2. Membutuhkan solusi komunikasi berbasis ethernet untuk menghubungkan 2 titik atau lebih yang terpisah satu sama lain\n" \
                   "3. Membutuhkan wifi yang dapat digunakan oleh pelanggan\n" \
                   "4. Membutuhkan monitoring untuk internet\n" \
                   "5. Membutuhkan ERP dengan modul HC/ Finance/ Procurement\n" \
                   "6. Membutuhkan monitoring keamanan lokasi\n" \
                   "7. Membutuhkan WA/ SMS blast untuk notifikasi/ alert untuk service"
                await update.message.reply_text(question)
                return BENGKEL_1
            elif number == 2:
                question = "Usaha automotive (bengkel) anda tidak memiliki cabang. Apa keluhan usaha anda?\n\n" \
                   "1. Membutuhkan internet untuk operasional bisnis\n" \
                   "2. Membutuhkan wifi dengan sistem voucher yang dapat dijual ke pelanggan bengkel\n" \
                   "3. Membutuhkan monitoring keamanan lokasi\n" \
                   "4. Membutuhkan sistem kasir sederhana (untuk pencatatan transaksi, reporting, dll)\n" \
                   "5. Ingin memiliki metode pembayaran yang universal melalui QRIS generator"
                await update.message.reply_text(question)
                return BENGKEL_2
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return JENIS_BENGKEL
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return JENIS_BENGKEL

async def bengkel_1_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 7:
            if number == 1:
                await solution_astinet(update=update, context=context)
                return ConversationHandler.END
            elif number == 2:
                await solution_metro(update=update, context=context)
                return ConversationHandler.END
            elif number == 3:
                await solution_wms(update=update, context=context)
                return ConversationHandler.END
            elif number == 4:
                await solution_netmonk(update=update, context=context)
                return ConversationHandler.END
            elif number == 5:
                await solution_erp(update=update, context=context)
                return ConversationHandler.END
            elif number == 6:
                await solution_indibiz_cam(update=update, context=context)
                return ConversationHandler.END
            elif number == 7:
                await solution_oca(update=update, context=context)
                return ConversationHandler.END
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return BENGKEL_1
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return BENGKEL_1

async def bengkel_2_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 4:
            if number == 1:
                await solution_hsi(update=update, context=context)
                return ConversationHandler.END
            elif number == 2:
                await solution_indibiz_wifi(update=update, context=context)
                return ConversationHandler.END
            elif number == 3:
                await solution_indibiz_cam(update=update, context=context)
                return ConversationHandler.END
            elif number == 4:
                await solution_indibiz_pay(update=update, context=context)
                return ConversationHandler.END
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return BENGKEL_2
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return BENGKEL_2

# DEALER
async def jenis_dealer_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 8:
            if number == 1:
                await solution_astinet(update, context)
                return ConversationHandler.END
            elif number == 2:
                await solution_metro( update, context)
                return ConversationHandler.END
            elif number == 3:
                await solution_netmonk( update, context)
                return ConversationHandler.END
            elif number == 4:
                await solution_finpay( update, context)
                return ConversationHandler.END
            elif number == 5:
                await solution_indibiz_cam( update, context)
                return ConversationHandler.END
            elif number == 6:
                await solution_oca( update, context)
                return ConversationHandler.END
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return JENIS_DEALER
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return JENIS_DEALER

# BARBER
async def jenis_barber_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 2:
            if number == 1:
                question = "Usaha barbershop/salon anda memiliki beberapa cabang. Apa keluhan usaha anda?\n\n" \
                   "1. Membutuhkan jaringan internet yg lebih stabil\n" \
                   "2. Membutuhkan internet yang dapat digunakan untuk operasional salon dan wifi yang dapat digunakan oleh pelanggan salon yang dapat dimonitor\n" \
                   "3. Membutuhkan monitoring untuk menjaga keamanan lokasi salon\n" \
                   "4. Membutuhkan sistem kasir yang lebih advance (hingga ke fitur table management) \n" \
                   "5. Membutuhkan WA blast untuk menginfokan promo yang sedang berlangsung ke pelanggan"
                await update.message.reply_text(question)
                return BARBER_1
            elif number == 2:
                question = "Usaha barbershop/salon anda tidak memiliki cabang. Apa keluhan usaha anda?\n\n" \
                   "1. Membutuhkan wifi yang dapat digunakan untuk operasional salon dan untuk pelanggan (bisa di provide oleh pemilik, bisa di jual melalui sistem voucher)\n" \
                   "2. Ingin memiliki metode pembayaran yang universal melalui QRIS generator\n" \
                   "3. Membutuhkan sistem kasir yang  dapat mengakomodir hingga ke barcode"
                await update.message.reply_text(question)
                return BARBER_2
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return JENIS_BARBER
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return JENIS_BARBER

async def barber_1_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 5:
            if number == 1:
                await solution_astinet(update=update, context=context)
                return ConversationHandler.END
            elif number == 2:
                await solution_hsi(update=update, context=context)
                return ConversationHandler.END
            elif number == 3:
                await solution_indibiz_cam(update=update, context=context)
                return ConversationHandler.END
            elif number == 4:
                await solution_indibiz_kasir(update=update, context=context)
                return ConversationHandler.END
            elif number == 5:
                await solution_oca(update=update, context=context)
                return ConversationHandler.END
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return BARBER_1
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return BARBER_1

async def barber_2_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 3:
            if number == 1:
                await solution_wms(update=update, context=context)
                return ConversationHandler.END
            elif number == 2:
                await solution_indibiz_pay(update=update, context=context)
                return ConversationHandler.END
            elif number == 3:
                await solution_indibiz_kasir(update=update, context=context)
                return ConversationHandler.END
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return BARBER_2
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return BARBER_2

# FASHION
async def jenis_fashion_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 2:
            if number == 1:
                question = "Usaha fashion/boutique anda memiliki beberapa cabang. Apa keluhan usaha anda?\n\n" \
                   "1. Membutuhkan internet untuk operasional toko yang dapat di monitor\n" \
                   "2. Membutuhkan  sistem pembayaran yang lebih advance (dengan fitur payment gateway, BI RTGS, Transfer dana, Uang elektronik, Debit acquirer, Quick Respon (QR) Code, Wallet) atau Ingin memiliki metode pembayaran yang universal melalui QRIS generator\n" \
                   "3. Membutuhkan monitoring keamanan lokasi\n" \
                   "4. Membutuhkan sistem kasir yang lebih advance (hingga ke fitur table management)"
                await update.message.reply_text(question)
                return FASHION_1
            elif number == 2:
                question = "Usaha fashion/boutique anda tidak memiliki cabang. Apa keluhan usaha anda?\n\n" \
                   "1. Membutuhkan internet untuk operasional toko\n" \
                   "2. Membutuhkan monitoring keamanan lokasi toko\n" \
                   "3. Ingin memiliki metode pembayaran yang universal melalui QRIS generator\n" \
                   "4. Membutuhkan sistem kasir yang  dapat mengakomodir hingga ke barcode"
                await update.message.reply_text(question)
                return FASHION_2
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return JENIS_FASHION
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return JENIS_FASHION

async def fashion_1_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 4:
            if number == 1:
                await solution_hsi(update=update, context=context)
                return ConversationHandler.END
            elif number == 2:
                await solution_finpay(update=update, context=context)
                return ConversationHandler.END
            elif number == 3:
                await solution_indibiz_cam(update=update, context=context)
                return ConversationHandler.END
            elif number == 4:
                await solution_indibiz_kasir(update=update, context=context)
                return ConversationHandler.END
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return FASHION_1
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return FASHION_1

async def fashion_2_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 4:
            if number == 1:
                await solution_hsi(update=update, context=context)
                return ConversationHandler.END
            elif number == 2:
                await solution_indibiz_cam(update=update, context=context)
                return ConversationHandler.END
            elif number == 3:
                await solution_indibiz_pay(update=update, context=context)
                return ConversationHandler.END
            elif number == 4:
                await solution_indibiz_kasir(update=update, context=context)
                return ConversationHandler.END
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return FASHION_2
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return FASHION_2

# LAUNDRY
async def jenis_laundry_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 2:
            if number == 1:
                question = "Usaha laundry anda memiliki beberapa cabang. Apa keluhan usaha anda?\n\n" \
                   "1. Membutuhkan internet untuk operasional toko yang dapat dimonitor\n" \
                   "2. Membutuhkan monitoring keamanan lokasi toko\n" \
                   "3. Ingin memiliki metode pembayaran yang universal melalui QRIS generator serta fitur untuk mencetak struk\n" \
                   "4. Membutuhkan sistem POS simple"
                await update.message.reply_text(question)
                return LAUNDRY_1
            elif number == 2:
                question = "Usaha laundry anda tidak memiliki cabang. Apa keluhan usaha anda?\n\n" \
                   "1. Membutuhkan internet untuk operasional toko\n" \
                   "2. Ingin memiliki metode pembayaran yang universal melalui QRIS generator\n" \
                   "3. Membutuhkan sistem POS simple\n" \
                   "4. Membutuhkan  WA blast untuk menginfokan promo ke para pelanggannya"
                await update.message.reply_text(question)
                return LAUNDRY_2
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return JENIS_LAUNDRY
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
    return ConversationHandler.END

async def laundry_1_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 4:
            if number == 1:
                await solution_hsi(update=update, context=context)
                return ConversationHandler.END
            elif number == 2:
                await solution_indibiz_cam(update=update, context=context)
                return ConversationHandler.END
            elif number == 3:
                await solution_indibiz_pay(update=update, context=context)
                return ConversationHandler.END
            elif number == 4:
                await solution_indibiz_pay(update=update, context=context)
                return ConversationHandler.END
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return LAUNDRY_1
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return LAUNDRY_1

async def laundry_2_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 4:
            if number == 1:
                await solution_hsi(update=update, context=context)
                return ConversationHandler.END
            elif number == 2:
                await solution_indibiz_pay(update=update, context=context)
                return ConversationHandler.END
            elif number == 3:
                await solution_indibiz_pay(update=update, context=context)
                return ConversationHandler.END
            elif number == 4:
                await solution_oca(update=update, context=context)
                return ConversationHandler.END
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return LAUNDRY_2
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return LAUNDRY_2

# GADGET
async def jenis_gadget_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 2:
            if number == 1:
                question = "Usaha Gadget & Elektronik anda memiliki beberapa cabang. Apa keluhan usaha anda?\n\n" \
                   "1. Membutuhkan internet untuk operasional toko\n" \
                   "2. Membutuhkan monitoring untuk menjaga keamanan lokasi toko\n" \
                   "3. Ingin memiliki metode pembayaran yang universal melalui QRIS generator\n" \
                   "4. Membutuhkan sistem pembayaran dan kasir sederhana (untuk pencatatan transaksi, reporting, dll)"
                await update.message.reply_text(question)
                return GADGET_1
            elif number == 2:
                question = "Usaha Gadget & Elektronik anda tidak memiliki cabang. Apa keluhan usaha anda?\n\n" \
                   "1. Membutuhkan internet untuk operasional toko\n" \
                   "2. Membutuhkan monitoring untuk menjaga keamanan lokasi toko\n" \
                   "3. Membutuhkan sistem pembayaran dan kasir sederhana (untuk pencatatan transaksi, reporting, dll)\n" \
                   "4. Ingin memiliki metode pembayaran yang universal melalui QRIS generator"
                await update.message.reply_text(question)
                return GADGET_2
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            JENIS_GADGET
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return JENIS_GADGET

async def gadget_1_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 4:
            if number == 1:
                await solution_hsi(update=update, context=context)
                return ConversationHandler.END
            elif number == 2:
                await solution_indibiz_cam(update=update, context=context)
                return ConversationHandler.END
            elif number == 3:
                await solution_indibiz_pay(update=update, context=context)
                return ConversationHandler.END
            elif number == 4:
                await solution_indibiz_pay(update=update, context=context)
                return ConversationHandler.END
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return GADGET_1
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return GADGET_1

async def gadget_2_func(update, context):
    user_answer = update.message.text.strip()
    if user_answer.isdigit():
        number = int(user_answer)
        if number >= 1 and number <= 4:
            if number == 1:
                await solution_hsi(update=update, context=context)
                return ConversationHandler.END
            elif number == 2:
                await solution_indibiz_cam(update=update, context=context)
                return ConversationHandler.END
            elif number == 3:
                await solution_indibiz_cam(update=update, context=context)
                return ConversationHandler.END
            elif number == 4:
                await solution_indibiz_pay(update=update, context=context)
                return ConversationHandler.END
        else:
            await update.message.reply_text("Tidak ada pilihan pada nomor tersebut.")
            return GADGET_2
    else:
        await update.message.reply_text("Silahkan pilih nomor sesuai dengan pilihan yang disediakan.")
        return GADGET_2

## SOLUTIONS
# DIGITAL CONNECTIVITY
async def solution_hsi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk HSI/Indibiz\n"\
            "Ketahui lebih lanjut mengenai produk HSI/Indibiz pada https://myindibiz.co.id/produk/indibiz-internet"
    await context.bot.send_message(chat_id=user_id, text=text)
    await exit_func(update, context)

async def solution_astinet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk Astinet\n"\
            "Ketahui lebih lanjut mengenai produk Astinet pada https://mycarrier.telkom.co.id/id/astinet"
    await context.bot.send_message(chat_id=user_id, text=text)
    await exit_func(update, context)

async def solution_netmonk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk Netmonk\n"\
            "Ketahui lebih lanjut mengenai produk Netmonk pada https://netmonk.id/"
    await context.bot.send_message(chat_id=user_id, text=text)
    await exit_func(update, context)

async def solution_wms(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk WMS\n"\
            "Ketahui lebih lanjut mengenai produk WMS pada https://wifi.id/bisnis"
    await context.bot.send_message(chat_id=user_id, text=text)
    await exit_func(update, context)

async def solution_metro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk Metro E\n"\
            "Ketahui lebih lanjut mengenai produk Metro E pada https://mycarrier.telkom.co.id/id/metro-ethernet"
    await context.bot.send_message(chat_id=user_id, text=text)
    await exit_func(update, context)

async def solution_indibiz_wifi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk Indibiz Wifi\n"\
            "Ketahui lebih lanjut mengenai produk Indibiz Wifi pada https://myindibiz.co.id/produk/indibiz-voucher-wifi"
    await context.bot.send_message(chat_id=user_id, text=text)
    await exit_func(update, context)

# DIGITAL PLATFORM
async def solution_finpay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk Finpay\n"\
           "Ketahui lebih lanjut mengenai produk Finpay pada https://finpay.id/"
    await context.bot.send_message(chat_id=user_id, text=text)
    await exit_func(update, context)

async def solution_flou(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk Flou\n" \
           "Ketahui lebih lanjut mengenai produk Flou pada https://floucloud.id/"
    await context.bot.send_message(chat_id=user_id, text=text)
    await exit_func(update, context)

async def solution_erp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk ERP\n"\
            "Ketahui lebih lanjut mengenai produk ERP pada https://telkom.co.id/sites/enterprise/id_ID/page/enterprise-resource-planning-288"
    await context.bot.send_message(chat_id=user_id, text=text)
    await exit_func(update, context)

async def solution_dms(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk DMS\n"\
            "Ketahui lebih lanjut mengenai produk DMS pada https://www.telkom.co.id/sites/enterprise/id_ID/page/digital-media-communication-solution-821"
    await context.bot.send_message(chat_id=user_id, text=text)
    await exit_func(update, context)

# DIGITAL SERVICE
async def solution_indibiz_cam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk Indibiz Cam\n"\
           "Ketahui lebih lanjut mengenai produk Indibiz Cam pada https://myindibiz.co.id/produk/ip-camera"
    await context.bot.send_message(chat_id=user_id, text=text)
    await exit_func(update, context)

async def solution_indibiz_pay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk Indibiz Pay\n"\
            "Ketahui lebih lanjut mengenai produk Indibiz Pay pada https://www.indibizpay.id/"
    await context.bot.send_message(chat_id=user_id, text=text)
    await exit_func(update, context)

async def solution_indibiz_kasir(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk Indibiz Kasir\n"\
            "Ketahui lebih lanjut mengenai produk Indibiz Kasir pada https://myindibiz.co.id/produk/indibiz-kasir"
    await context.bot.send_message(chat_id=user_id, text=text)
    await exit_func(update, context)

async def solution_oca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = "Berdasarkan profil usaha serta keluhan anda, anda dapat menggunakan produk OCA\n"\
            "Ketahui lebih lanjut mengenai produk OCA pada https://www.instagram.com/oca.indonesia/"
    await context.bot.send_message(chat_id=user_id, text=text)
    await exit_func(update, context)

# EXIT
async def exit_func(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = "Terimakasih sudah menggunakan Telkom SDA SME IS Bot.\n\n"\
            "klik /start untuk memulai kembali!"
    await update.message.reply_text(text)