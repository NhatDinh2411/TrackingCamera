import cv2
import os
import asyncio
import time
from uuid import uuid4
from pathlib import Path
from ultralytics import YOLO


class HumanTracker:
    def __init__(self, model_path, tracker_config, camera_source=0, conf_threshold=0.5):
        self.model_path = model_path
        self.tracker_config = tracker_config
        self.camera_source = camera_source
        self.conf_threshold = conf_threshold

        self.output_dir = Path("HumanImage")
        self.output_dir.mkdir(exist_ok=True)

        self.model = YOLO(model_path)

        self.human_dict = {}

    async def process_video_frame(self, frame, bot):

        results = self.model.track(
            frame,
            conf=self.conf_threshold,
            persist=True,
            tracker=self.tracker_config,
            classes=[0]
        )

        annotated_frame = results[0].plot()

        if results[0].boxes.id is not None:
            boxes = results[0].boxes.xyxy.cpu().numpy()
            ids = results[0].boxes.id.int().cpu().numpy()

            for i, human_id in enumerate(ids):
                hid = int(human_id)

                if hid not in self.human_dict:
                    x1, y1, x2, y2 = map(int, boxes[i])

                    if x1 >= x2 or y1 >= y2 or x1 < 0 or y1 < 0:
                        continue

                    human_crop = frame[y1:y2, x1:x2]

                    filename = self.output_dir / f"detected_#{human_id}.jpg"
                    cv2.imwrite(str(filename), human_crop)

                    if bot:
                        await bot.send_image(str(filename), caption=f"New human detected: #{human_id}")

                    self.human_dict[hid] = {"first_seen": time.time()}

        return annotated_frame

    async def process_frames(self, bot):
        cap = cv2.VideoCapture(self.camera_source)

        if not cap.isOpened():
            print("Lỗi: Không thể kết nối với camera")
            return

        self.running = True

        try:
            while self.running:
                success, frame = cap.read()

                if not success:
                    print("Không thể đọc frame từ camera")
                    break
                annotated_frame = await self.process_video_frame(frame, bot)

                cv2.imshow("YOLO11 Tracking", annotated_frame)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

        except Exception as e:
            print(f"Lỗi xảy ra trong quá trình xử lý video: {e}")
        finally:
            cap.release()
            cv2.destroyAllWindows()
            self.running = False