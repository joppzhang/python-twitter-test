#coding=utf-8
import time
#-------------------------------------
u={} #用户名-uid
t={} #发布时间-消息id
day={} #天数
dm={}#每个小时对应的消息数量
du={}#每天那个用户发布最多
with open("twitter.txt",'rb') as f:
	lines = f.readlines()
	for line in lines:
		line =line.decode('utf-8')
		w = line.split(",")
		t[w[0]]=w[6]
		u[w[1]]=w[2]
		try:
			d = time.strptime(w[6],'"%Y-%m-%d %H:%M:%S"')
			du_date = "{}-{}-{} {} {}".format(d.tm_year,d.tm_mon,d.tm_mday,w[1],w[2])
			date = "{}".format(d.tm_hour)
			if du_date in du:
				du[du_date]=du[du_date]+1
			else:
				du[du_date]=1
			if date in dm:
				dm[date]=dm[date]+1
			else:
				dm[date]=1
		except Exception:
			continue

	f.close()
#用户数量
print("用户数量：{}".format(len(u)))
#---------------------------------------
#打印用户id和名字
print(u)
#--------------------------------------
#11月推特数量
#print(t)
#w[6]就是time  t {id:time}
count = 1
for date in t:
	try:
		d = time.strptime(t[date],'"%Y-%m-%d %H:%M:%S"')
		if d.tm_mon == 11:
			count+=1
	except Exception:
		continue
print("11月的消息数量是：{}".format(count))
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
#统计每个小时发布的消息数量
#dm就是时间小时为键，数量为值，排序就可以了
p = zip(dm.values(),dm.keys())#转换为元组排序
print(sorted(p))
#--------------------------------------
#每一天发布推特最多的用户
#把每一天日期+用户id作为键，微博数量为值。循环遍历相同日期下
#数量最大的值存入新的字典，日期为键，用户为值
# day_messages=zip(du.values(),du.keys())
# print(sorted(day_messages))
du_result={}
temp_key=0
for du_date in du:
	key = du_date.split(' ')
	if key[0] in du_result:
		if temp_key==0:
			temp_key=du_date
		if du[du_date] > du[temp_key]:
			du_result[key[0]]=key[2]
			temp_key = du_date
	else:
		du_result[key[0]]=key[2]
		temp_key = du_date
print(du_result)
#----------------------------------------
#2012-11-03每小时推特数量
