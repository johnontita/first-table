"""
Write a query that will display the results below 
(Note: some columns might be renamed but use the column names above). 
It should only show 2020 data and order by driver points.
"""
import pymysql
connecting=pymysql.connect(user='root',password='',host='localhost',database='teach_give')
#getting a cursor :it is used to iterate the rest of a select statement
cursoring=connecting.cursor() 
record_one="insert into driver_info values('portimao',1,1,63, 26,'Lewis Hamilton', 'portugues grand prix','1:29:56.828',2020,'mercedes','2020-10-25')"
record_two="insert into driver_info values('Sochi',3,1,51,26,'Valtein Buttas','Russian Grand prix','1:34:00:364',2020,'mercedes','2020-09-27')"
record_three="insert into driver_info values('Imola',2,1,63,26,'Lewis Hamilton','Emilia Grand Prix','1:28:32.430',2020,'mercedes','2020-09-27')"
record_four="insert into driver_info values('Budapest',1,1,70,26,'Lewis Hamilton','Hungarian grand prix','1:36:12.473',2020,'mercedes','2020-11-01')"
record_five="insert into driver_info values('Mugello',1,1,58,26,'Lewis Hamilton','Tuscan grand prix','2:19:35.062',2020,'mercedes','2020-07-19')"
record_six="insert into driver_info values('Sakhir',5,1,67,25,'Sergio Perez','Sakhir grand prix','1:31:15.114',2020,'racing puin','2020-12-06')"
record_seven="insert into driver_info values('Nurbug',2,1,58,25,'Lewis Hamilton','Eifel grand prix','1:35:49.641',2020,'mercedes','2020-10-11')"
record_eight="insert into driver_info values('Speilburg',1,1,68,25,'Lewis Hamilton','Styrian grand prix','1:22:50.683',2020,'mercedes','2020-07-12')"
record_nine="insert into driver_info values('Sakhir',1,1,38,25,'Lewis Hamilton','Bahrain grand prix','2:59:47.515',2020,'mercedes','2020-11-29')"
record_ten="insert into driver_info values('Monza',10,1,34,25,'pierre Gasly','Italian grand prix','1:47:06.056',2020,'AlphaTauni','2020-09-06')"
record_eleven="insert into driver_info values('Monza',10,1,34,25,'pierre Gasly','Italian grand prix','1:47:06.056',2020,'AlphaTauni','2020-09-06')"
record_twelve="insert into driver_info values('Silverstone',4,1,46,25,'max verstappen','70th aniversary grand prix','1:19:41.993',2020,'Red Bull','2020-08-09')"
record_thirteen="insert into driver_info values('Spielburg',1,1,68,25,'Valteri Dottas','Australian grand prix','1:30:55.739',2020,'mercedes','2020-07-05')"
record_fourteen="insert into driver_info values('Istanbul',6,1,56,25,'Lewis Hamilton','Turkish Grand prix','1:42:19.313',2020,'mercedes','2020-08-02')"
record_fifteen="insert into driver_info values('SilverStone',1,1,45,25,'Lewis Hamilton','British grand prix','1:28-01-283',2020,'mercedes','2020-08-02')"

data=cursoring.execute(record_one)
data=cursoring.execute(record_two)
data=cursoring.execute(record_three)
data=cursoring.execute(record_four)
data=cursoring.execute(record_five)
data=cursoring.execute(record_six)
data=cursoring.execute(record_seven)
data=cursoring.execute(record_eight)
data=cursoring.execute(record_nine)
data=cursoring.execute(record_ten)
data=cursoring.execute(record_eleven)
data=cursoring.execute(record_twelve)
data=cursoring.execute(record_thirteen)
data=cursoring.execute(record_fourteen)
data=cursoring.execute(record_fifteen)
#sends q quit
connecting.close()