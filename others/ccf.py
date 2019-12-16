#-*- coding: utf-8 -*-
import random as rd
n = 50
print('%d 3' %n)
for i in range(n//2):
	print("{} {} {}".format(rd.randint(20,50),rd.randint(20,50),0))
for i in range(n//2):
	print("{} {} {}".format(rd.randint(40,70),rd.randint(40,70),1))	