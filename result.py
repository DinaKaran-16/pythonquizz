#!C:\Python312\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import pymysql

db = pymysql.Connection(host="localhost",user="root",password="sqldina",database="user_database")
cur = db.cursor()
cur.execute("select * from user_register")
for i in cur:
    name = i[0]

f = cgi.FieldStorage()
q1= f.getvalue("q1")
q2 = f.getvalue("q2")
q3 = f.getvalue("q3")
q4 = f.getvalue("q4")
q5 = f.getvalue("q5")
q6 = f.getvalue("q6")
q7 = f.getvalue("q7")
q8 = f.getvalue("q8")
q9 = f.getvalue("q9")
q10 = f.getvalue("q10")
q11 = f.getvalue("q11")
q12 = f.getvalue("q12")
q13 = f.getvalue("q13")
q14 = f.getvalue("q14")
q15 = f.getvalue("q15")
q16 = f.getvalue("q16")
q17 = f.getvalue("q17")
q18 = f.getvalue("q18")
q19 = f.getvalue("q19")
q20 = f.getvalue("q20")

mark = 0
not_attended = 0
wrong_answer = 0

if not q1:
    not_attended+=1
elif q1!="ans2":
    wrong_answer+=1
else:
    mark+=1
    
if not q2:
    not_attended+=1
elif q2!="ans2":
    wrong_answer+=1
else:
    mark+=1
    
if not q3:
    not_attended+=1
elif q3!="ans1":
    wrong_answer+=1
else:
    mark+=1
    
if not q4:
    not_attended+=1
elif q4!="ans1":
    wrong_answer+=1
else:
    mark+=1

if not q5:
     not_attended+=1

elif q5!="ans3":
    wrong_answer+=1
else:
    mark+=1    
if not q6:
     not_attended+=1
 
elif q6!="ans3":
    wrong_answer+=1
else:
    mark+=1
    
if not q7:
     not_attended+=1
elif q7!="ans2":
    wrong_answer+=1
else:
    mark+=1
    
if not q8:
     not_attended+=1
elif q8!="ans2":
    wrong_answer+=1
else:
    mark+=1
if not q9:
     not_attended+=1
elif q9!="ans2":
    wrong_answer+=1
else:
    mark+=1
    
if not q10:
     not_attended+=1
elif q10!="ans2":
    wrong_answer+=1
else:
    mark+=1
if not q11:
     not_attended+=1
elif q11!="ans1":
    wrong_answer+=1
else:
    mark+=1
if not q12:
     not_attended+=1
elif q12!="ans2":
    wrong_answer+=1
else:
    mark+=1

if not q13:
     not_attended+=1
elif q13!="ans1":
    wrong_answer+=1
else:
    mark+=1
    
if not q14:
     not_attended+=1
elif q14!="ans3":
    wrong_answer+=1
else:
    mark+=1
    
if not q15:
     not_attended+=1
elif q15!="ans2":
    wrong_answer+=1
else:
    mark+=1
if not q16:
     not_attended+=1
elif q16!="ans2":
    wrong_answer+=1
else:
    mark+=1
    
if not q17:
     not_attended+=1

elif q17!="ans3":
    wrong_answer+=1
else:
    mark+=1
    
if not q18:
     not_attended+=1
elif q18!="ans2":
    wrong_answer+=1
else:
    mark+=1
    
if not q19:
     not_attended+=1
elif q19!="ans2":
    wrong_answer+=1
else:
    mark+=1
if not q20:
    not_attended+=1
elif q20!="ans1":
    wrong_answer+=1
else:
    mark+=1

print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("<title>Python Quiz</title>")
print("<style>")
print("body {")
print("background-image: url('http://localhost/Mainproject/image9.jpg');")  # Path to your background image
print("background-size: cover;")
print("background-attachment: fixed;")
print("}")
print("</style>")
print("</head>")
print("<body>")
print("<h1><center>")
print("Hello ",name,"<br><br>")
print("Mark is "+str(mark)+"<br>")
print("wrong answer"+str(wrong_answer)+"<br>")
print("Questions not attended: " + str(not_attended))
print("</center></h1>")
print("</body>")
print("</html>")


