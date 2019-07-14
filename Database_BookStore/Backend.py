import sqlite3 as sq

class Database:
    def __init__(self,dbname):
        self.conn=sq.connect(dbname)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE if not exists Book(id INTEGER PRIMARY KEY,Title text ,Author text,Year INTEGER, ISBN INTEGER )")
        self.conn.commit()

    def insert_data(self,Title,Author,Year,ISBN):
        self.t=(Title,Author,Year,ISBN)
        self.cur.execute("INSERT into Book VALUES (NULL,?,?,?,?)",self.t)
        self.conn.commit()
        print("Data inserted")

    def view_data(self):
        self.cur.execute("SELECT * FROM Book")
        rows=self.cur.fetchall()
        return rows

    def search_data(self,Title="",Author="",Year="",ISBN=""):
        self.t=(Title,Author,Year,ISBN)
        self.cur.execute("SELECT * FROM Book where Title=? OR Author=? OR Year=? OR ISBN=?",self.t)
        rows=self.cur.fetchall()
        return rows

    def delete_data(self,id):
        self.cur.execute("DELETE FROM Book where id =?",(id,))
        self.conn.commit()

    def update_data(self,id,Title,Author,Year,ISBN):
        self.t1=(Title,Author,Year,ISBN,id)
        self.cur.execute("UPDATE Book SET Title=?,Author=?,Year=?,ISBN=? WHERE id=?",self.t1)
        self.conn.commit()
#d=Database()
#d.connection('Book.db')
#d.insert_data('Between a Rock and a Hard Place',2004,'Aron Ralston',1245)        
