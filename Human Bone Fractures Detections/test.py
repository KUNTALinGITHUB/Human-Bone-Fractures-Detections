import cv2
import os
from ultralytics import YOLO

# Load the YOLO model
model = YOLO(r"E:\Kuntal\project_idea\my_Projects\Human Bone Fractures Detection\runs\detect\train\weights\best.pt")

# Load a single image
image_path = r"E:\Kuntal\project_idea\my_Projects\Human Bone Fractures Detection\Dataset\test\images\20_mri_0_3663_jpeg.rf.987f2271c9fd05767274b3c17f7ec281.jpg"
image = cv2.imread(image_path)

# Run YOLO inference on the image
results = model(image)

# Visualize the results
annotated_image = results[0].plot()

# Display the annotated image
cv2.imshow("YOLOv8 - Single Image Test", annotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the annotated image
output_path = r"E:\Kuntal\project_idea\my_Projects\Human Bone Fractures Detection\outputs"
os.makedirs(output_path, exist_ok=True)
output_file = os.path.join(output_path, "annotated_result1.jpg")

cv2.imwrite(output_file, annotated_image)
print(f"Result saved to {output_file}")
