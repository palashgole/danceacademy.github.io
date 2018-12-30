#!c:/Python35/python.exe
print("Content-Type: text/html")

print("<h1>Welcome to my acadmey</h1>")
print("<h1>Welcome to my acadmey</h1>")
      
import mysql.connector,cgi
db=mysql.connector.connect(host="localhost",user="root",password="mysql@158",database="drjbp")
cursor=db.cursor()

form=cgi.FieldStorage()

name=form.getvalue("name")
dob=form.getvalue("dt")
mblno=form.getvalue("mno")
gen=form.getvalue("gen")
city=form.getvalue("city")
unm=form.getvalue("unm")
pwd=form.getvalue("pwd")

query=("insert into patient values(%s,%s,%s,%s,%s,%s,%s)")
val=(name,dob,mblno,gen,city,unm,pwd)
cursor.execute(query,val)
db.commit()

