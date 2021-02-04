import mysql.connector

class Connection:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host = 'localhost', database = 'employees', user = 'root')
            self.cur = self.con.cursor()
        except Exception as e:
            print(e)
    def getExcecute(self,query):
        try:
            self.cur.execute(query)
            for row in self.cur.fetchall():
                yield row
        except Exception as e:
            print(e)
    def closeCon(self):
        try:
            self.cur.close()
            self.con.close()
        except Exception as e:
            print(e)



if __name__ == '__main__':
   obj = Connection()

str = input('Enter the query to be executed :')
ans = obj.getExcecute(str)
for row in ans:
    print(row)
obj.closeCon()
print("Connection is Closed!!")