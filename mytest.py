import mysql.connector as x 

testmydatabase=x.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root"
)

mycursor = testmydatabase.cursor()

data = mycursor.execute("SHOW DATABASES")

fetchRow = mycursor.fetchall()

print("current data is {0}".format(fetchRow[0]))

print(fetchRow)
print(type(fetchRow))


dict ={
  "List_database":fetchRow,
  "activate show database":
}
print("print data ",dict["List_database"][0])

print(type(dict["List_database"][0]))

tuple_converstion = dict["List_database"][0][0]
print(tuple_converstion)

Database_select_input=None


for x in range(len(dict["List_database"])):
    print("select your database " , dict["List_database"][x][0])
    Database_select_input=input("enter your data input")
    if(input==dict["List_database"][x][0]):
        print("you have selected your database",dict["List_database"][x][0])
    else:
        print("the database sorry")
        print("please create database")
        input






