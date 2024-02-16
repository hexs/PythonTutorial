from ultralytics import YOLO

model = YOLO('yolov8m.yaml')  # เป็นการสร้างโมเดลใหม่ขึ้นมา

# โหลด pretrained model มาเพื่อให้เราไม่ต้องเทรนใหม่ทั้งหมดตั้งแต่เริ่ม
# model = YOLO(r'C:\Python_Project\yolo8\train_find_a_white_hat\runs\detect\train5\weights\last.pt')

path = 'data.yaml'
results = model.train(data=path, epochs=600)

# ทดสอบโมเดลโดยใช้ validation datasets ที่เตรียมไว้
results = model.val()

# เซฟโมเดลโดยให้โมเดลอยู่ใน ONNX format
success = model.export(format='onnx')

print(results)
print(success)
