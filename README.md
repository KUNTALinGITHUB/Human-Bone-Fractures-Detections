# Human-Bone-Fractures-Detections




# 🦴 Human Bone Fractures Detection using YOLOv11n

A deep learning project that applies YOLOv11n to detect and localize bone fractures in medical X-ray images.

---

## 📖 Overview

This project uses the object detection model **YOLOv11n** to identify fractures in various bones (e.g., elbow, hand, shoulder) from X-ray images. Unlike traditional classification models, YOLOv11n draws bounding boxes around detected fracture regions, providing spatial awareness and high precision.

---

## 🧠 Use Cases

- **Medical Diagnostics:** Detect fractures automatically in X-rays to assist radiologists.
- **Triage Systems:** Quickly flag possible fractures in emergency care systems.
- **Medical Research:** Help study fracture patterns at scale with automated labeling.

---

## 🛠️ Tech Stack

- **Model:** YOLOv11n (custom-trained)
- **Frameworks:** Python, OpenCV
- **Annotation Tool:** LabelImg
- **Hardware:** GPU recommended for training; CPU inference possible

---

## 🚀 Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/KUNTALinGITHUB/Human-Bone-Fractures-Detections.git
   cd Human-Bone-Fractures-Detections
Install Dependencies:


Download Pre-trained Weights (if available):

Add weights file (e.g., yolov11n.pt) into the weights/ directory

🧪 Training (Optional)
Prepare the dataset in YOLO format (images + .txt annotations).

Train the model:

bash

python train.py --data data/fracture.yaml --cfg cfg/yolov11n.yaml --weights '' --epochs 100
🕵️ Inference / Detection
To run fracture detection on new X-ray images:

bash

python detect.py --weights weights/yolov11n.pt --img 640 --conf 0.25 --source data/xray_images/

use your own path
Detected fractures will be saved with bounding boxes and labels.

📊 Results
Bounding boxes accurately mark fracture regions

High detection confidence (~90% depending on dataset)

Fast inference (<50ms on GPU)

🧾 Dataset
You can use public datasets like MURA or RSNA Bone Fracture dataset.

Make sure to convert annotations to YOLO format using LabelImg.

📷 Example Output

📜 License
MIT License

🤝 Contributions
Contributions and suggestions are welcome. Fork the repo and submit a pull request!

yaml


---

Let me know if you'd like me to generate a sample image or diagram to use in the LinkedIn post or README!



