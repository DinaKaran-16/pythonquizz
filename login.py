#!C:\Python312\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import pymysql
import loginquizz

f = cgi.FieldStorage()

def login(email_id,E_password):
    db = pymysql.Connection(host="localhost",user="root",password="sqldina",database="user_database")
    cur = db.cursor()
    mn = f.getvalue("email_id")
    p1 =f.getvalue("password")
    query = "SELECT * FROM user_register WHERE email_id=%s AND E_password=%s"
    
    val =(mn,p1)
    cur.execute(query,val)
    user= cur.fetchone()
    db.commit()

    if user:
        print(loginquizz.pythonquizz())


    
        
login("example@email.com", "password123")





'''
db = pymysql.Connection(host="localhost",user="root",password="sqldina",database="user_database")
cur = db.cursor()

mn = f.getvalue("email_id")

p1 =f.getvalue("password")
    
query = ("SELECT * FROM user_register WHERE email_id=%s AND E_password=%s",(email_id,E_password)
user = cur.fetchone()
if email_id==emai_id and E_password==E_password:
    print(one.quizz)
else:
    print("invalid")
             

val =(mn,p1)
cur.execute(query,val)
db.commit()
'''
