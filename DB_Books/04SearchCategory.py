import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',password='skodabmw',database='bookstoredb')
curs=con.cursor()

category=input('Enter the category : ')
curs.execute("select BookName from books where Category='%s'"%category)
data=curs.fetchall()
books=[]
for rec in data:
    books.append(rec[0])
print(books)