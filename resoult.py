#coding=utf-8
import time
#-------------------------------------
u={} #用户名-uid
t={} #发布时间-消息id
day={} #天数
with open("twitter.txt",'rb') as f:
	lines = f.readlines()
	for line in lines:
		line =line.decode('utf-8')
		w = line.split(",")
		t[w[0]]=w[6]
		u[w[1]]=w[2]
	f.close()
#用户数量
# print("用户数量：{}".format(len(u)))
#---------------------------------------
#打印用户id和名字
#print(u)
#--------------------------------------
#11月推特数量
#print(t)
#w[6]就是time  t {id:time}
# count = 1
# for date in t:
# 	try:
# 		d = time.strptime(t[date],'"%Y-%m-%d %H:%M:%S"')
# 		if d.tm_mon == 11:
# 			count+=1
# 	except Exception:
# 		continue
# print("11月的消息数量是：{}".format(count))
#--------------------------------------
#计算一共几个日期
for date in t:
	try:
		d = time.strptime(t[date],'"%Y-%m-%d %H:%M:%S"')
		date = "{}-{}-{}".format(d.tm_year,d.tm_mon,d.tm_mday)
		day[date]=1
	except Exception:
		continue
print(len(day))
days=['' for i in range(len(day))]
i=0
for s in day:
	days[i]=s
	i=i+1
print(days)
#--------------------------------------
#那个小时发布消息最多
#