import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',password='skodabmw',database='bookstoredb')
curs=con.cursor()

try:
    code=int(input("Enter BookCode : "))
    curs.execute("select * from books where BookCode=%d"%code)
    data=curs.fetchall()

    if data:
        amt=float(input("Enter new price : "))
        curs.execute("update books set Price_Rs = %.2f"%amt)
        con.commit()
        print("Data updated successfully")
    else:
        print("Book not found")
except:
    print("enter valid data")
con.close()