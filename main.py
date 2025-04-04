import asyncio
import os
import threading
from dotenv import load_dotenv
from TelegramCalling.telegramBot import TelegramBotWithImageSender
from Tracking.Tracking import HumanTracker

load_dotenv('.env')

MODEL_PATH = "Tracking/models/yolo11n_openvino_model"
TRACKER_CONFIG = "Tracking/models/botsort.yaml"
CAMERA_IP = os.environ.get('CAMERA_IP')

TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')


if __name__ == "__main__":
    bot = TelegramBotWithImageSender(token=TOKEN, chat_id=CHAT_ID)

    if CAMERA_IP is None:
        CAMERA_IP = 0

    tracker = HumanTracker(
        model_path=MODEL_PATH,
        tracker_config=TRACKER_CONFIG,
        camera_source=CAMERA_IP,
        conf_threshold=0.5,
    )

    asyncio.run(tracker.process_frames(bot))