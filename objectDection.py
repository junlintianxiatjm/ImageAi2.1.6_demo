# 物体检测，提取和微调（有输出图，且标有检测框）
# 虚拟环境: tf37_imageai2_1_6_env
# 参考资料： https://imageai-cn.readthedocs.io/zh_CN/latest/ImageAI_Object_Detection.html#


from imageai.Detection import ObjectDetection

import os
import time

# 计时
start = time.time()

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(os.path.join(execution_path, "./h5/yolo-tiny.h5"))

detector.loadModel()

# 将检测后的结果保存为新图片

# 同时指定多个对象执行检测
custom_objects = detector.CustomObjects(car=True, motorcycle=True)
detections, objects_path = detector.detectObjectsFromImage(custom_objects=custom_objects,
                                                           input_image=os.path.join(execution_path, "traffic.jpg"),
                                                           output_image_path=os.path.join(execution_path,
                                                                                          "traffic2new.jpg"),
                                                           extract_detected_objects=True)

# 全部可检测对象
# detections, objects_path = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "person.jpg"),
#                                                            output_image_path=os.path.join(execution_path,
#                                                                                           "person2new.jpg"),
#                                                            extract_detected_objects=True,
#                                                            minimum_percentage_probability=80)

# detections, objects_path = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "x3.jpg"),
#                                                            output_image_path=os.path.join(execution_path,
#                                                                                           "x3new.jpg"),
#                                                            extract_detected_objects=True,
#                                                            minimum_percentage_probability=50)

# 结束计时
end = time.time()

# 预测物体名:预测概率:物体两点坐标（左上，右下）
for eachObject in detections:
    print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ",
          eachObject["box_points"])
    print("--------------------------------")

# =================================================================

for eachObject, eachObjectPath in zip(detections, objects_path):
    print(eachObject["name"], " : ", eachObject["percentage_probability"])
    print("Object's image saved in ", eachObjectPath)
    print("--------------")

print("cost time:", end - start)

# person  :  82.6427161693573
# Object's image saved in  D:\python-workspace\ImageAi2.1.6_demo\person2new.jpg-objects\person-2.jpg
# --------------
# person  :  84.69338417053223
# Object's image saved in  D:\python-workspace\ImageAi2.1.6_demo\person2new.jpg-objects\person-3.jpg
# --------------
# cost time: 4.786202430725098
#
# Process finished with exit code 0

# ======================================================================

# 2021-01-22 16:38:03.535181: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:116] None of the MLIR optimization passes are enabled (registered 2)
# car  :  51.1025071144104  :  [0, 64, 112, 107]
# --------------------------------
# person  :  89.28637504577637  :  [202, 51, 270, 209]
# --------------------------------
# person  :  70.36035656929016  :  [255, 55, 332, 201]
# --------------------------------
# person  :  50.62069296836853  :  [85, 58, 171, 253]
# --------------------------------
# car  :  51.1025071144104
# Object's image saved in  D:\python-workspace\ImageAi2.1.6_demo\traffic2new.jpg-objects\car-1.jpg
# --------------
# person  :  89.28637504577637
# Object's image saved in  D:\python-workspace\ImageAi2.1.6_demo\traffic2new.jpg-objects\person-2.jpg
# --------------
# person  :  70.36035656929016
# Object's image saved in  D:\python-workspace\ImageAi2.1.6_demo\traffic2new.jpg-objects\person-3.jpg
# --------------
# person  :  50.62069296836853
# Object's image saved in  D:\python-workspace\ImageAi2.1.6_demo\traffic2new.jpg-objects\person-4.jpg
# --------------
# cost time: 4.901922702789307
#
# Process finished with exit code 0
