
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database='reserve'
)

cursor = mydb.cursor()

def check_reserve_time(start,end,worker_id):
  sql = "SELECT * FROM reserve.reservation where str_rez <= %s and end_rez >= %s and worker_id=%s"
  values = [end,start,worker_id]
  cursor.execute(sql,values)
  myresult = cursor.fetchall()
  data = []
  for each in myresult:
    data.append(each)
  return data

def make_reservation(start,end,customer_phone,worker_id):
  sql = "insert into reservation (str_rez,end_rez,customer_phone,worker_id) values (%s,%s,%s,%s)"
  values = [start,end,customer_phone,worker_id]
  cursor.execute(sql,values)
  mydb.commit()

def get_reservation_by_by_worker_id(worker_id):
  sql = "select * from reservation where worker_id=%s "
  values = [worker_id]
  cursor.execute(sql,values)
  result = cursor.fetchall()
  data = []
  for each in result:
    data.append(each)
  return data
