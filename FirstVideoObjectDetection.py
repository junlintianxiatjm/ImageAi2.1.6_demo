# ImageAI：视频对象检测和跟踪
# 虚拟环境: tf37_imageai2_1_6_env
# 参考资料：https://imageai-cn.readthedocs.io/zh_CN/latest/ImageAI_Video_Object_Detection_and_Tracking.html


from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(os.path.join(execution_path, "./h5/yolo-tiny.h5"))
detector.loadModel()

video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "football.mp4"),
                                             output_file_path=os.path.join(execution_path, "football_detected"),
                                             frames_per_second=20, log_progress=True)
print(video_path)
