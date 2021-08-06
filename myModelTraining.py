# ImageAI：自定义预测模型训练--图像分类问题（数据量要大，训练次数要多，模型准确率才能高，预测才可用）
# 虚拟环境: tf37_imageai2_1_6_env
# 参考资料：https://imageai-cn.readthedocs.io/zh_CN/latest/ImageAI_Custom_Prediction_Model_Training.html#


from imageai.Prediction.Custom import ModelTraining

model_trainer = ModelTraining()
model_trainer.setModelTypeAsInceptionV3()
model_trainer.setDataDirectory("fruits")
model_trainer.trainModel(num_objects=4, num_experiments=50, enhance_data=True, batch_size=10,
                         show_network_summary=True)

# Epoch 19/20
# 26/26 [==============================] - 28s 1s/step - loss: 0.5599 - accuracy: 0.7691 - val_loss: 0.7708 - val_accuracy: 0.6667
#
# Epoch 00019: accuracy did not improve from 0.77922
# Epoch 20/20
# 26/26 [==============================] - 26s 1s/step - loss: 0.7952 - accuracy: 0.6980 - val_loss: 0.9154 - val_accuracy: 0.6111
#
# Epoch 00020: accuracy did not improve from 0.77922
#
# Process finished with exit code 0
