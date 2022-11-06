import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler

from PIL import Image, ImageDraw, ImageFont
import time

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
    
async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    tm_mday=time.gmtime().tm_mday
    tm_mon=time.gmtime().tm_mon
    tm_year=time.gmtime().tm_year
    tm_hour=time.gmtime().tm_hour + 3
    tm_min=time.gmtime().tm_min
    stamp=(f'{tm_mday}.{tm_mon}.{tm_year} {tm_hour}-{tm_min}')
    image = Image.open("some_cat.jpeg")
    font = ImageFont.truetype("arial.ttf", 150)
    drawer = ImageDraw.Draw(image)
    drawer.text((600, 700), stamp, font=font, fill='red')
    image.save('cat_with_datetime.jpeg')
    await context.bot.sendPhoto(chat_id=update.effective_chat.id, photo=open('cat_with_datetime.jpeg', 'rb'))    

if __name__ == '__main__':
    application = ApplicationBuilder().token('5562077909:AAGJR_369p9rnGjr2McPV0PTGnzjZmSs8T8').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()
