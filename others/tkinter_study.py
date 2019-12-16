import tkinter as tk
import pymysql as ps
import pandas as pd
num = 1
def select_from(place):
	sql = "select * from studentinfo1 where bornplace='{}'".format(place)
	cur.execute(sql)
	data = cur.fetchall()
	return data
def count_bornplace():
	data = select_from(var_bornplace_input.get())
	info.delete('1.0','end')
	info.insert('end',len(data))
def print_bornplace():
	data = select_from(var_bornplace_input.get())
	info.delete('1.0','end')
	info.insert('end',pd.DataFrame(list(data),columns=['学号','姓名','性别','籍贯','成绩']))
def delete_database():
	sql1 = "create table studentinfo{} like studentinfo".format(num)
	sql2 = "drop table studentinfo"
	sql3 = "select * from studentinfo1 where bornplace='{}'".format(var_bornplace_input.get())
	cur.execute(sql1)
	cur.execute(sql2)
	cur.execute(sql3)
	data = cur.fetchall()
	info.delete('1.0','end')
	info.insert('end',pd.DataFrame(list(data),columns=['学号','姓名','性别','籍贯','成绩']))
def muti_table():
	sql_3 = "select teac.教师 from stud,relation,teac where (stud.姓名='{}') and (stud.学号=relation.学号) and (relation.课程=teac.课程名)".format(var_bornplace_input.get())
	cur.execute(sql_3)
	data = cur.fetchall()
	info.delete('1.0','end')
	info.insert('end',pd.DataFrame(list(data)))
	
conn = ps.connect(host='127.0.0.1',user='root',passwd='zhaojunnan213315',port=3306,db='dbmcbase',charset='utf8')
cur = conn.cursor()

window = tk.Tk()
window.title('XingYou_MySql')
window.geometry('400x300')

var_bornplace_input = tk.StringVar()
bornplace_input = tk.Entry(window,textvariable=var_bornplace_input,font=('Arial',28))
bornplace_input.pack()
bornplace_input.place(x=0,y=0)
count_button = tk.Button(window,text='count',font=('Arial',20),width=4,height=1,command=count_bornplace)
print_button = tk.Button(window,text='print',font=('Arial',20),width=4,height=1,command=print_bornplace)
delete_creat_button = tk.Button(window,text='delete',font=('Arial',20),width=4,height=1,command=delete_database)
search_button = tk.Button(window,text='search',font=('Arial',20),width=4,height=1,command=muti_table)
#insert_button = tk.Button(window,text='insert',font=('Arial',20),width=4,height=1,command=insert_info)
count_button.pack()
count_button.place(x=1,y=80)
print_button.pack()
print_button.place(x=100,y=80)
delete_creat_button.pack()
delete_creat_button.place(x=200,y=80)
search_button.pack()
search_button.place(x=300,y=80)
info = tk.Text(window,height=11)
info.pack()
info.place(x=1,y=200)
window.mainloop()

cur.close()