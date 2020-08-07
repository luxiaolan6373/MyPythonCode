import cv2
'''
第一个参数当然就是图像的路径，第二个参数用户指定图像读取的模式：JYZnWl O
>I?S*_h]b21N!&qnVkM}QHyB
cv2.IMREAD_COLOR -- 默认，载入一个彩色图像，忽略透明度
cv2.IMREAD_GRAYSCALE -- 载入一个灰阶图像
cv2.IMREAD_UNCHANGED -- 载入一个包含 Alpha 通道（透明度）的图像
你也可以使用 1, 0, -1 三个整数代替上面三种方式。
'''
img=cv2.imread(r'C:\Users\Administrator\Desktop\Background\ysn.jpg',0)
print(img.shape)#尺寸
#修改尺寸 宽 高
img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
print(img.shape)#尺寸
#创建一个窗口显示图片
cv2.imshow('ysn',img)
#进程等待键盘响应 单位毫秒 0表示一直等待
k=cv2.waitKey(0)
#按下S关闭q
if k==27:#esc键
    #关闭窗口
    cv2.destroyWindow('ysn')
elif k==115:#S键
    #保存文件
    cv2.imwrite(r'C:\Users\Administrator\Desktop\Background\ysn1.jpg',img)


