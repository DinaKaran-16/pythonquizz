#!C:\Python312\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import pymysql
import one

f = cgi.FieldStorage()
db = pymysql.Connection(host="localhost",user="root",password="sqldina",database="user_database")
cur = db.cursor()

fn = f.getvalue("username")
mn = f.getvalue("email_id")

p1 =f.getvalue("password")



query = "insert into user_register(username,email_id,E_password) values (%s,%s,%s)"

val =(fn,mn,p1)
cur.execute(query,val)
db.commit()
one.quizz()
