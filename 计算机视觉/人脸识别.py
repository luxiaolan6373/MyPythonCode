import cv2
#载入一个图
img=cv2.imread(r"C:\Users\Administrator\Desktop\Background\tim.jpg",1)
#转换成灰阶图
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#创建一个级联分类器对象 载入官方通过大数据将人脸的特征转换为数值的一个文件。
face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
#搜索图像的坐标
'''
这里几个参数给大家解释一下：
image -- 需要检测人脸的图像
scaleFactor -- 该参数指定每次图像缩小的比例
minNeighbors -- 该参数指定每一个目标至少要被检测到多少次
'''
faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 10)

#在人脸位置画个框框标记一下 一张图有可能有多个人,所以要循环识别和标记
for x, y, w, h in faces:
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow('g', img)
k=cv2.waitKey(0)