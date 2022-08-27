import os
import mysql.connector as sql
userName=os.environ.get("DB_USER")
userpass=os.environ.get("DB_PASS")
try:
    mydb=sql.connect(host='localhost',
                    user=userName,
                    passwd=userpass,
                    database="dbase")
    cursor=mydb.cursor()
except:
    print("Some error occured. Try again later....")

if mydb.is_connected():
        query="create table if not exists product_master (product_no varchar(6) primary key,description varchar(15) not null,profit_percent double(4,2) not null,unit_measure varchar(10) not null,qty_on_hand int(8) not null,reorder_lvl int(8) not null,sell_price double(8,2) not null,cost_price double(8,2) not null);"
        cursor.execute(query)
        product_no=input("Enter Product Number: ")
        description=input("Enter description: ")
        profit_percent=float(input("Enter profit percent: "))
        unit_measure=input("Enter unit measure: ")
        qty_on_hand=int(input("Enter Qty: "))
        reorder_lvl=int(input("Enter reorder level: "))
        sell_price=float(input("Enter sell price: "))
        cost_price=float(input("Enter cost price: "))
        if product_no.startswith("P") and sell_price !=0 and cost_price !=0:
            query=f"insert into product_master values('{product_no}','{description}',{profit_percent},'{unit_measure}',{qty_on_hand},{reorder_lvl},{sell_price},{cost_price});"
            cursor.execute(query)
            mydb.commit()
        else:
            print("Enter details properly....")