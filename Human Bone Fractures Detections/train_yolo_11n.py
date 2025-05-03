from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data= "E:/Kuntal/project_idea/my_Projects/Human Bone Fractures Detection/classes.yaml", epochs=40)