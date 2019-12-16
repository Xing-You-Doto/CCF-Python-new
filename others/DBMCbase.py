from random import *
number = [i for i in range(1001,1026)]
class_number = [i for i in range(2000,2010)]
first_name = ['张','王','李','赵','刘','高','魏','曹','秦','方']
second_name = ['一','二','三','四','五','六','七','八','九','白']
sex = ['男','女']
age = [x for x in range(17,22)]
class_ = ['一','二','三','四']
course = ['语文','英语','数学','化学','物理','计算机','生物','网络','系统','Python']
teacher = ['师一','师二','师三']
n = 10
'''
for i in range(20):
	print('('+str(1006+i)+','+"'"+first_name[int(random()*10)]+second_name[int(random()*10)] \
		+"'"+','+"'"+sex[int(random()*2)]+"'"+','+str(age[int(random()*5)])+','+"'"+class_[int(random()*4)]+"'"+')'+',')
'''
aa = 2000
'''
for i in range(10):
	print('('+str(aa+i)+','+"'"+str(course[i])+"'"+','+"'"+str(teacher[int(random()*3)])+"'"+')'+',')
'''
m = 80
for i in range(m):
	print('('+str(number[int(random()*25)])+','+"'"+str(course[int(random()*10)])+"'"+')'+',')

