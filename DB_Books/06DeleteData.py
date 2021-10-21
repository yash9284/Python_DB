import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',password='skodabmw',database='bookstoredb')
curs=con.cursor()

try:
    code=int(input("Enter BookCode : "))
    curs.execute("select * from books where BookCode=%d"%code)
    data=curs.fetchone()
    print('BookName = %s'%data[1])
    print('Category = %s'%data[2])
    print('Author = %s'%data[3])
    print('Publication = %s'%data[4])
    print('Edition = %d'%data[5])
    print('Price_Rs = %.2f'%data[6])

    l=input("Do you want to delete the book : ")
    if data:
        if l.upper()=='YES':
            curs.execute("delete from books where BookCode=%d"%code)
            con.commit()
            print("Book deleted successfully")
        else:
            print("Ok;No Problem!")
except:
    print("Invalid data or code not exist")    
con.close()    