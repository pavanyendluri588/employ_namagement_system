import mysql.connector

class Database:
    def __init__(self, db):
        self.mydb = mysql.connector.connect(host='localhost',user='root',passwd='1234',database='employee')
        #self.mydb = sqlite3.mydbnect(db)
        self.cur = self.mydb.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary Key,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            mydbtact text,
            address text
        )
        """
        self.cur.execute(sql)
        self.mydb.commit()

    # Insert Function
    def insert(self, name, age, doj, email, gender, mydbtact, address):
        self.cur.execute("insert into employees(name,age,doj,gender,email,mydbtact,address) values (%s,%s,%s,%s,%s,%s,%s)",
                         (name, age, doj, email, gender, mydbtact, address))
        self.mydb.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from employees")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from employees where id=?", (id,))
        self.mydb.commit()

    # Update a Record in DB
    def update(self, id, name, age, doj, email, gender, mydbtact, address):
        self.cur.execute(
            "update employees set name=%s, age=%s, doj=%s, email=%s, gender=%s, mydbtact=%s, address=%s where id=%s",
            (name, age, doj, email, gender, mydbtact, address, id))
        self.mydb.commit()