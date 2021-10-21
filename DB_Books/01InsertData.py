import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='skodabmw',database='bookstoredb')
curs=con.cursor()

try:
    code=int(input('Enter BookCode : '))
    nm=input("Enter the book name : ")
    category=input("Enter the category : ")
    author=input("Enter the Author name : ")
    publication=("Enter thr Publication : ")
    edt=int(input("Enter the Edition : "))
    price=float(input("Enter the price : "))

    curs.execute("insert into books values(%d,'%s','%s','%s','%s',%d,%.2f)" %(code,nm,category,author,publication,edt,price))
    con.commit()
    print('Book added successfully')

except:
    print('cant take data...invalid input,duplicate bookcode')  

con.close()      

