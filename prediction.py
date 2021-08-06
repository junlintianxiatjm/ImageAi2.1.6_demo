# imageai训练yolov3模型，目标检测
# 虚拟环境: tf37_imageai2_1_6_env


from imageai.Detection.Custom import DetectionModelTrainer

# 定义模型训练器
trainer = DetectionModelTrainer()
# 设置网络类型
trainer.setModelTypeAsYOLOv3()
# 设置要在其上训练网络的图像数据集的路径
trainer.setDataDirectory(data_directory="pets")
trainer.setTrainConfig(object_names_array=["dog", "cat"], batch_size=3, num_experiments=10,
                       )
# 当训练用于检测多个对象时，设置object_names_array=["object1", "object2", "object3",..."objectz"]
trainer.trainModel()

# 2021-01-21 17:13:26.027449: I tensorflow/core/profiler/lib/profiler_session.cc:172] Profiler session tear down.
# 24/24 [==============================] - 189s 8s/step - loss: 614.6321 - yolo_layer_loss: 70.0805 - yolo_layer_1_loss: 140.1457 - yolo_layer_2_loss: 392.8295 - val_loss: 126.9683 - val_yolo_layer_loss: 19.5068 - val_yolo_layer_1_loss: 38.5215 - val_yolo_layer_2_loss: 57.3625
# Epoch 2/13
# 24/24 [==============================] - 193s 8s/step - loss: 229.2987 - yolo_layer_loss: 32.0997 - yolo_layer_1_loss: 48.6139 - yolo_layer_2_loss: 137.0074 - val_loss: 119.9941 - val_yolo_layer_loss: 17.0106 - val_yolo_layer_1_loss: 32.6784 - val_yolo_layer_2_loss: 58.7267
# Epoch 3/13
# 24/24 [==============================] - 178s 7s/step - loss: 129.7384 - yolo_layer_loss: 14.6134 - yolo_layer_1_loss: 24.9484 - yolo_layer_2_loss: 78.5988 - val_loss: 104.1370 - val_yolo_layer_loss: 13.2555 - val_yolo_layer_1_loss: 25.5435 - val_yolo_layer_2_loss: 53.7642
# .
# .
# .
# .
# Epoch 11/13
# 24/24 [==============================] - 182s 8s/step - loss: 42.6567 - yolo_layer_loss: 5.6325 - yolo_layer_1_loss: 5.7698 - yolo_layer_2_loss: 20.0560 - val_loss: 36.5416 - val_yolo_layer_loss: 2.6981 - val_yolo_layer_1_loss: 4.3966 - val_yolo_layer_2_loss: 18.3205
# Epoch 12/13
# 24/24 [==============================] - 162s 7s/step - loss: 35.2561 - yolo_layer_loss: 2.7483 - yolo_layer_1_loss: 4.4980 - yolo_layer_2_loss: 16.9069 - val_loss: 35.5212 - val_yolo_layer_loss: 2.9796 - val_yolo_layer_1_loss: 3.9102 - val_yolo_layer_2_loss: 17.5997
# Epoch 13/13
# 24/24 [==============================] - 177s 7s/step - loss: 37.4558 - yolo_layer_loss: 4.7005 - yolo_layer_1_loss: 4.1206 - yolo_layer_2_loss: 17.6251 - val_loss: 35.4262 - val_yolo_layer_loss: 3.2093 - val_yolo_layer_1_loss: 4.4339 - val_yolo_layer_2_loss: 16.8253
#
# Process finished with exit code 0
