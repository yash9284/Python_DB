import mysql.connector as mycon
con=mycon.connect(host='localhost',user='root',password='skodabmw',database='bookstoredb')
curs=con.cursor()
try:
    auth=input("Enter Author name : ")
    pub=input("Enter publication name : ")

    curs.execute("select BookName from books where Author='%s' and Publication='%s'"%(auth,pub))
    data=curs.fetchall()
    l=[]
    if data:
        for rec in data:
            l.append(rec[0])
        print(l)
    else:    
        print("Invalid data")
    con.close()       
except Exception as e:
    print(e)
    print("Invalid input")
