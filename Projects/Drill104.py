
import os
import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


def create():
    conn = sqlite3.connect('Drill.db')
    with conn:
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_List(\
            ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, \
            col_book TEXT\
            )")
        conn.commit()
    conn.close()

def cycle():
    conn = sqlite3.connect('Drill.db')
    with conn:
        for filename in fileList:
            if filename.endswith('.txt'):
                if filename.endswith('.txt'):
                    cur=conn.cursor()
                    cur.execute("INSERT INTO tbl_List(col_book) VALUES(?)",(filename,))
                    print(filename)
    conn.close()
            
if __name__ =="__main__":
    create()
    cycle()
