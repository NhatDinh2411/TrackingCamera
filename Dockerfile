FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    libglib2.0-0 libsm6 libxext6 libxrender-dev \
    libopencv-dev ffmpeg libgl1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /CameraTracking

COPY . /CameraTracking

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Chạy ứng dụng
CMD ["python", "main.py"]