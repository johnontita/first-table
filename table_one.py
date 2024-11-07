import pymysql
conne=pymysql.Connect(user='root',password="",host="localhost",database="querry_py")
cursor=conne.cursor()
record_one="insert into table_one values('John ontita','Ece',25,'four')"
record_two="insert into table_one values('Joshua','Ece',22,'four')"
record_three="insert into table_one values('Ruth','Ece',22,'four')"
# r=cursor.execute(record_one)
r=cursor.execute(record_two)
r=cursor.execute(record_three)