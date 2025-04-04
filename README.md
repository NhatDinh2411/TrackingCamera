# 🧠 Human Tracker with YOLO + Telegram Bot

A human detection and tracking app using YOLO to identify and track people through a camera. It automatically sends images to Telegram when a new person is detected.

---

## 🚀 Features

- 📦 Human detection using YOLOv11
- 🧍 Multi-person tracking (multi-id)
- 🤖 Send images via Telegram bot when a new person is detected
- 🐳 Can run with either Python (venv) or Docker

---

## 📁 Project Structure
```bash
CameraTracking/
├── main.py                # Main entry point
├── telegram_bot.py        # Controls the Telegram bot
├── human_tracker.py       # YOLO + tracking handling class
├── requirements.txt       # Required libraries
├── Dockerfile             # For running with Docker
├── .dockerignore          # Files to ignore during Docker build
└── HumanImage/            # Folder to store detected human images
```
---
# ⚙️ Telegram Bot Setup
1.	Create a bot through @BotFather
2.	Retrieve the token and insert it into the code (.env)
3.	Get your chat_id by either chatting with the bot or using the Bot API

# 🧑‍💻 1. Running with Python + Virtualenv

## ✏️ Step 1: Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # For Linux/macOS
venv\Scripts\activate         # For Windows
```
## 📦 Step 2: Install dependencies
```bash
pip install -r requirements.txt
```
## ▶️ Step 3: Run the app
```bash
python main.py
```

# 🐳 2. Running with Docker
## 📦 Step 1: Build the Docker image
```bash
docker build -t human-tracker-bot
```
## ▶️ Step 2: Run the Docker container
```bash
docker run --rm human-tracker-bot
```
👉 If you’re using a camera on Linux:
```bash
docker run --rm --device=/dev/video0 human-tracker-bot
```


# 📌 Notes
- Detected images are saved in the HumanImage/ folder.
-	Press q in the display window to exit the program.
