# 自定义目标检测，待开发......



from imageai.Detection import ObjectDetection

import os
import time

# 计时
start = time.time()

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()

# 载入已训练好的文件
detector.setModelPath(os.path.join(execution_path, "./pets/models/detection_model-ex-007--loss-0041.253.h5"))
detector.loadModel()

# 将检测后的结果保存为新图片
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "d.jpg"),
                                             output_image_path=os.path.join(execution_path, "image3new.jpg"))

# 结束计时
end = time.time()

for eachObject in detections:
    print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ",
          eachObject["box_points"])  ##预测物体名:预测概率:物体两点坐标（左上，右下）
    print("--------------------------------")

print("\ncost time:", end - start)
