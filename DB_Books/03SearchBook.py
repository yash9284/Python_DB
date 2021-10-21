import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',password='skodabmw',database='bookstoredb')
curs=con.cursor()

no=int(input("Enter the BookCode : "))
curs.execute("select BookName,Category,Author,Publication,Edition,Price_Rs from books where BookCode=%d"%no)
rec=curs.fetchone()

try:
    print('BookName = %s'%rec[0])
    print('Category = %s'%rec[1])
    print('Author = %s'%rec[2])
    print('Publication = %s'%rec[3])
    print('Edition = %d'%rec[4])
    print('Price_Rs = %.2f'%rec[5])
except:
    print('Book does not found.')    
con.close()

