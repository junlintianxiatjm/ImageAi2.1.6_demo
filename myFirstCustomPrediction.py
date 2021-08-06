# 自定义模型预测--图像分类
# 虚拟环境: tf37_imageai2_1_6_env


from imageai.Prediction.Custom import CustomImagePrediction
import os

execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsInceptionV3()
prediction.setModelPath(os.path.join(execution_path, "./fruits/models/model_ex-037_acc-0.987500.h5"))
prediction.setJsonPath(os.path.join(execution_path, "./fruits/json/model_class.json"))
prediction.loadModel(num_objects=4)

predictions, probabilities = prediction.predictImage(image_input=os.path.join(execution_path, "p1.jpg"), result_count=4)

for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction, " : ", eachProbability)

# 2021-01-22 14:52:53.233290: I tensorflow/compiler/jit/xla_gpu_device.cc:99] Not creating XLA devices, tf_xla_enable_xla_devices not set
# D:/python-workspace/ImageAi2.1.6_demo/myFirstCustomPrediction.py:16: MatplotlibDeprecationWarning: '.predictImage()' has been deprecated! Please use 'classifyImage()' instead.
#   predictions, probabilities = prediction.predictImage(image_input=os.path.join(execution_path, "p1.jpg"), result_count=4)
# 2021-01-22 14:52:54.832078: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:116] None of the MLIR optimization passes are enabled (registered 2)
# pear  :  75.21457076072693
# orange  :  20.698879659175873
# banana  :  2.441956102848053
# apple  :  1.6445951536297798
#
# Process finished with exit code 0
