# 应用训练的模型做目标检测
# 虚拟环境: tf37_imageai2_1_6_env


from imageai.Detection.Custom import CustomObjectDetection

detector = CustomObjectDetection()
# 创建该类实例，并将模型类型设置为YOLOv3
detector.setModelTypeAsYOLOv3()
# 指定了模型文件的文件路径
detector.setModelPath("./dogs/models/detection_model-ex-007--loss-0041.253.h5")
# 指定了detection_config.json文件的路径
detector.setJsonPath("./dogs/json/detection_config.json")
# 并在第三行中加载了模型
detector.loadModel()
# 运行了detectObjectsFromImage()函数并解析了测试图像的路径以及该函数将保存的新图像的路径。然后，该函数返回一个字典数组，每个字典对应于图像中检测到的对象数
detections = detector.detectObjectsFromImage(input_image="d.jpg", output_image_path="d-detected.jpg")

for detection in detections:
    # 每个字典都具有属性name（对象的名称）， percentage_probability（检测的概率百分比）和box_points（对象的边界框的x1，y1，x2和y2坐标）。
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
