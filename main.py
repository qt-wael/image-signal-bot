# Telegram bot with automatic RSI & Stochastic analysis from image
import os
import cv2
import pytesseract
import logging
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Path to tesseract (edit if needed)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # or 'C:/Program Files/Tesseract-OCR/tesseract.exe'

BOT_TOKEN = "YOUR_TOKEN_HERE"

# OCR & Analysis

def extract_rsi_stochastic_text(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

def analyze_text(text):
    lines = text.splitlines()
    rsi_value = None
    stochastic_desc = "غير واضح"
    trend = "غير محدد"

    for line in lines:
        if "RSI" in line.upper():
            digits = [s for s in line.split() if s.replace('.', '', 1).isdigit()]
            if digits:
                rsi_value = float(digits[0])

        if "ستوكاستيك" in line or "Stochastic" in line:
            if "تقاطع" in line or "cross" in line:
                stochastic_desc = line.strip()

    if rsi_value is not None:
        if rsi_value < 30:
            rsi_note = "تشبع بيع"
            recommendation = "شراء"
        elif rsi_value > 70:
            rsi_note = "تشبع شراء"
            recommendation = "بيع"
        else:
            rsi_note = "محايد"
            recommendation = "انتظار"
    else:
        rsi_value = "غير معروف"
        rsi_note = "غير واضح"
        recommendation = "غير محدد"

    return f"🔍 التحليل الفني:\n- RSI = {rsi_value} ({rsi_note})\n- Stochastic {stochastic_desc}\n- الاتجاه: {trend}\n✅ التوصية: {recommendation} في بداية الشمعة القادمة"

# Telegram bot handler
async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_file = await update.message.photo[-1].get_file()
    image_path = f"received_{update.message.message_id}.jpg"
    await photo_file.download_to_drive(image_path)

    text = extract_rsi_stochastic_text(image_path)
    analysis = analyze_text(text)

    await update.message.reply_text(analysis)
    os.remove(image_path)

# Run the bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))
    app.run_polling()
