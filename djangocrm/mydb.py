import mysql.connector

dataBase= mysql.connector.connect(host='localhost',user='root',passwd='T@rkesh@2512')

cursorObject=dataBase.cursor()

cursorObject.execute("Create Database elderco")

print("Al Done")
