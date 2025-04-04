import os
import asyncio
from threading import Thread
from telegram import Update, Bot, InputFile
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    Application
)

class TelegramBotWithImageSender:
    def __init__(self, token: str, chat_id: str):
        self.token = token
        self.chat_id = chat_id
        self.bot = Bot(token=self.token)
        self.app: Application = ApplicationBuilder().token(self.token).build()

    async def send_image(self, image_path: str, caption: str = "Có người xuất hiện !!!"):
        if not os.path.exists(image_path):
            print(f"❌ Không tìm thấy ảnh: {image_path}")
            return
        try:
            with open(image_path, "rb") as img:
                await self.bot.send_photo(
                    chat_id=self.chat_id,
                    photo=InputFile(img),
                    caption=caption
                )
            print(f"✅ Ảnh đã gửi: {image_path}")
        except Exception as e:
            print(f"⚠️ Lỗi gửi ảnh: {e}")

    def run(self):
        print("🚀 Bot Telegram đang chạy...")
        self.app.run_polling()

