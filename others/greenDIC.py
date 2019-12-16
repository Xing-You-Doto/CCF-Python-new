str1 = input()
flag = 0
str2 = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

while True:
	for i in str2:
		x = str1.find(i)
		if x == -1:
			continue
		else:
			if x < 4:
				continue
			else:
				if str1[x-4:x].isdigit():
					print(str1[x-4:x+3])
					flag = 0
	if flag == 1:
		print('2000Jan')
		break