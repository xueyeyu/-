import pandas as pd
import time

#有中文路径直接读取会出错
#csv_data = pd.read_csv(r'E:/第一课堂/毕业论文/思路/transcad/order_20161101')  # 读取训练数据

f=open(r'E:/第一课堂/毕业论文/思路/transcad/order_20161101')
csv_data=pd.read_csv(f,names=['DDID','starttime','endtime','startlon','startlat','endlon','endlat'])
#print(csv_data.info)

#查看前10行
#print(csv_data.head(10))
#检查数据是否有重复，false表示只有一次出现，如果有第二次出现会标记true
#print(csv_data.duplicated())
#print("*************")
#去重操作
data = csv_data.drop_duplicates()

#print(data.duplicated())
#检查data_dpcheck是否有true类型
data_dpcheck=data.duplicated()
for i in data_dpcheck:
	if i:
		print("wrong")
#时间用整型，便于计算。strftime可转为时间。



秒转时间
seconds =35400
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
print("%d:%02d:%02d" % (h, m, s))



