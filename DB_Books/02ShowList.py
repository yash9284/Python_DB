import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',password='skodabmw',database='bookstoredb')

curs=con.cursor()
curs.execute("select BookName from books")
data=curs.fetchall()
l=[]
for rec in data:
    l.append(rec[0])
print(l)    
    