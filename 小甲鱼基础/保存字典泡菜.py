import pickle
#保存字典到文件
zd={'a':1,'b':2,'c':3}
f= open(r'C:\Users\Administrator\Desktop\zd.pkl','wb')
pickle.dump(zd,f)
f.close()
#读取字典
f=open(r'C:\Users\Administrator\Desktop\zd.pkl','rb')
zd=pickle.load(f)
print(zd)