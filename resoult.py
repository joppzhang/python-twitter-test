#coding=utf-8
import time
 
#-------------------------------------
u={} #用户名-uid
t={} #发布时间-消息id
day={} #天数
dm={}#每个小时对应的消息数量
du={}#每天那个用户发布最多
minnum={}#20121103这天的每小时为键，每小时的数量为值
source={}#微博的客户端来源
message={'573638104':0}#用户573638104发了多少条微博

with open("twitter.txt",'rb') as f:
	lines = f.readlines()
	for line in lines:
		line =line.decode('utf-8')
		w = line.split(",")
		t[w[0]]=w[6]
		u[w[1]]=w[2]
		if w[1]=='"573638104"':
			message['573638104']=message['573638104']+1
		if w[7] in source:
			source[w[7]]=source[w[7]]+1
		else:
			source[w[7]]=1
		try:
			d = time.strptime(w[6],'"%Y-%m-%d %H:%M:%S"')
			if d.tm_year==2012 and d.tm_mon==11 and d.tm_mday==3:
				minnumkey = "2012-11-03 {}".format(d.tm_hour)
				if minnumkey in minnum:
					minnum[minnumkey]=minnum[minnumkey]+1
				else:
					minnum[minnumkey]=1
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
		except Exception as ex:
			# print(ex)
			continue
	f.close()
#用户数量
# print("用户数量：{}".format(len(u)))
#---------------------------------------
#打印用户id和名字
# print(u)
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
# for date in t:
# 	try:
# 		d = time.strptime(t[date],'"%Y-%m-%d %H:%M:%S"')
# 		date = "{}-{}-{}".format(d.tm_year,d.tm_mon,d.tm_mday)
# 		day[date]=1
# 	except Exception:
# 		continue
# print(len(day))
# days=['' for i in range(len(day))]
# i=0
# for s in day:
# 	days[i]=s
# 	i=i+1
# print(days)
#--------------------------------------
#那个小时发布消息最多
#统计每个小时发布的消息数量
#dm就是时间小时为键，数量为值，排序就可以了
# p = zip(dm.values(),dm.keys())#转换为元组排序
# print(sorted(p))
#--------------------------------------
#每一天发布推特最多的用户
#把每一天日期+用户id作为键，微博数量为值。循环遍历相同日期下
#数量最大的值存入新的字典，日期为键，用户为值
# day_messages=zip(du.values(),du.keys())
# print(sorted(day_messages))
# du_result={}
# temp_key=0
# for du_date in du:
# 	key = du_date.split(' ')
# 	if key[0] in du_result:
# 		if temp_key==0:
# 			temp_key=du_date
# 		if du[du_date] > du[temp_key]:
# 			du_result[key[0]]=key[2]
# 			temp_key = du_date
# 	else:
# 		du_result[key[0]]=key[2]
# 		temp_key = du_date
# print(du_result)
#----------------------------------------
#2012-11-03每小时推特数量
#以时间和小时为键，相同的时间值加以，不是这一天的pass
# l=[(0,0) for x in range(24)]
# i=0
# for x in minnum:
# 	d = x.split(" ")
# 	l[i]=(int(d[1])+1,int(minnum[x]))
# 	i=i+1
# print(sorted(l))
#-----------------------------------------
# w[7]就是微博的来源，取w[7]，然后相同的key值加1
#不同key赋值1
#因为数据格式不对的问题，获取时间等不一定是一样的列
# sourceresoult = zip(source.values(),source.keys())
# print(sorted(sourceresoult,reverse=True))
#------------------------------------------
#UID为573638104的用户 发了多少个微博
print(message)
#-------------------------------------------
#定义一个函数,放入任意多的用户uid参数
#（如果不存在则返回null），函数返回发微薄数最多的用户uid。
def maxmessageuid( *uid ):
	pass