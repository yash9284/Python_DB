import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',password='skodabmw',database='bookstoredb')
curs=con.cursor()
try:
    bcode=int(input("Enter the bookcode : "))
    curs.execute("select * from books where BookCode=%d"%bcode)
    data=curs.fetchone()

    if data:
        reviews=input('Enter review comments: ')
        curs.execute("update books set review='{p1}' where BookCode={p2}".format(p1=reviews,p2=bcode))
        con.commit()
        print('Review Updated Successfully')
    else:
        print('Book does not exist')
        con.close()
except Exception as e:
    print(e)
    print('Invalid input')
