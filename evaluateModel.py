# 物体检测，模型评估
# 虚拟环境: tf37_imageai2_1_6_env
# 参考资料： https://blog.csdn.net/qq_40784418/article/details/106038094


from imageai.Detection.Custom import DetectionModelTrainer

# 一、单一模型评估
# trainer = DetectionModelTrainer()
# trainer.setModelTypeAsYOLOv3()
# trainer.setDataDirectory(data_directory="pets")
# metrics = trainer.evaluateModel(model_path="pets/models/detection_model-ex-004--loss-0070.271.h5",
#                                 json_path="pets/json/detection_config.json",
#                                 iou_threshold=0.5, object_threshold=0.3, nms_threshold=0.5)

# 二、多模型评估
from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="pets")
metrics = trainer.evaluateModel(model_path="pets/models", json_path="pets/json/detection_config.json",
                                iou_threshold=0.5, object_threshold=0.3, nms_threshold=0.5)
