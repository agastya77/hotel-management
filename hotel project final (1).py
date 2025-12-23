import mysql.connector as sq
con=sq.connect(host="localhost",user="root",passwd="mysql")
if con.is_connected():
    print("**************************************************************************************************************************")
cursor=con.cursor()
##CREATING DATABASE
cursor.execute("create database if not exists hotel_record")
cursor.execute("use hotel_record")
##CREATING ADMIN TABLE
cursor.execute("create table if not exists admin_login(username varchar(50)not null, password varchar(25) not null)")
##CREATING CUSTOMER TABLE
cursor.execute("create table if not exists customer(cust_name varchar(50), cust_id varchar(25), room_no int, mode_of_payment varchar(20), check_in datetime, check_out datetime)")
##CREATING TABLE FOR USER INPUT PERSONAL DETAILS
cursor.execute("create table if not exists cust_personal(fname varchar(20), lname varchar(20), mobno int not null, id varchar(20) not null, dur int, persons int, rooms int, reservation_date datetime, suite varchar(5), floor varchar(10))")
con.commit()
##TO ENTER THE DETAILS FOR RESERVATION
def reserve():
    name=input("enter first name")
    lname=input("enter last name")
    no=int(input("enter mobile number"))
    if no==0000000000:
        print("mobile number cannot be null")
    cust_id=int(input("enter id: "))
    duration=int(input("enter the duration of stay"))
    pers=int(input("enter the no of persons"))
    rooms=int(input("enter the no of rooms required"))
    date=input("enter the date of check in")
    coup=input("would you like to view our suites: y/n")
    if coup=="y" or coup=="Y":
        print(''' ****WELCOME TO SUNRISE SUITES****
                exclusive suites for luxurious stay
            1. floor 19- comes with pool and access to premium lounge
            2. floor 20- comes with infinity pool and rooftop access with lounge and many other premium offers''')
        top=input("would you like to book our suite? y/n")
        if top=="y" or top=="Y":
            floor=input("please mention the floor")
            cursor.execute("insert into cust_personal values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,lname,no,cust_id,duration,pers,rooms,date,top,floor))
            con.commit()
            print("                    RESERVATION CONFIRMED                    ")
            print()
            print("                    THANK YOU FOR BOOKING IN SUNSHINE HOTEL                    ")
            print()
            print("                    ENJOY YOUR STAY AT SUNSHINE HOTEL                    ")
            print()
        else:
            top="n"
            floor="null"

            cursor.execute("insert into cust_personal values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,lname,no,cust_id,duration,pers,rooms,date,top,floor))
            con.commit()
            print("                    RESERVATION CONFIRMED                    ")
            print()
            print("                    THANK YOU FOR BOOKING IN SUNSHINE HOTEL                    ")
            print()
            print("                    ENJOY YOUR STAY AT SUNSHINE HOTEL                    ")
    else:
      conf=input("would you like to confirm your reservation: y/n")
      if conf=="y" or conf=="Y":
          top="n"
          floor="null"
          cursor.execute("insert into cust_personal values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,lname,no,cust_id,duration,pers,rooms,date,top,floor))
      con.commit()
      print("                    RESERVATION CONFIRMED                    ")
      print()
      print("                    THANK YOU FOR BOOKING IN SUNSHINE HOTEL                    ")
      print()
      print("                    ENJOY YOUR STAY AT SUNSHINE HOTEL                    ")

          
##reserve()

##DEFINING FUNCTIONS FOR ADMIN
      
def admin_handle():
    while True:
        print("WELCOME ADMIN")
        print("WHAT WOULD YOU LIKE TO DO TODAY?")
        print('''        1. add customer data

        2. edit customer data
        
        3. display all records
        
        4. delete a record
        
        5. search a record
        
        6.exit''')
        choice=int(input("enter choice of action"))
        if choice==1:
            ask=input("do you want to add a record? y/n")
            if ask=="y" or ask=="Y":
##calling function to insert                
                add_record()                                    
            else:
                print("please choose a course of action")
                continue
        elif choice==2:
            a=input("do you want to edit a record? y/n")
            if a=="y" or a=="Y":
##calling function to edit
                edit_record()                                    
            else:
                print("please choose a course of action")
                continue
        elif choice==3:
            s=input("do you wish to see all records? y/n")
            if s=="y" or s=="Y":
##calling function to display all records
                displayall()                                      
            else:
                print("please choose a course of action")
                continue
        elif choice==4:
            d=input("do you wish to delete customer record? y/n")
            if d=="y" or d=="Y":
##calling function to delete a record
                delete_record()                                    
            else:
                print("please choose a course of action")
                continue
        elif choice==5:
            w=input("do you wish to search a customer record? y/n")
            if w=="y" or w=="Y":
##calling function to search a record
                search_user()                                     
            else:
                print("please choose a course of action")
                continue
        elif choice==6:
            break

        
        else:
            
            print("Invalid choice. Please enter again")
            
##LOGGING IN AS ADMIN 
def admin():
    flag=0
    cursor.execute("select*from admin_login")
    for i in cursor:
        flag+=1
    if flag==0:
        cursor.execute("insert into admin_login values('admin','1234')")    #setting password for admin table
        con.commit()
    try: 
        user=input("enter username")
        pswrd=int(input("enter password"))
        cursor.execute("select*from admin_login")
        result=cursor.fetchone()
        if result:
            print("login successful")
            admin_handle()
        else:
            print("please enter valid username and password")
    except Exception as e:
        print(e)

##DEFINING FUNCTION TO ADD A RECORD

def add_record():
    try:
##        while ch=="Y" or ch=="y":
        cust_name=input("enter customer name")     #inserting customer records
        cust_id= input("enter id")
        room=int(input("enter room no"))
        pay=input("enter mode of payment")
        inn=input("date and time of check in(yyyy-mm-dd)")
        out=input("date and time of check out(yyyy-mm-dd)")
        cursor.execute("insert into customer values('{}','{}','{}','{}','{}','{}')".format(cust_name,cust_id,room,pay,inn,out))
        con.commit()
        print()
        print("record entered successfully")
##        ch=input("do u want to enter more records")
##        if ch=="Y" or ch=="y":
##            continue
##        else:
##            break
            
    except Exception as e:
        print(e)

####DEFINING FUNCTION TO EDIT A RECORD
        
def edit_record():
    try:
        c=input("enter the column name you wish to update")     #updating customer records  
        a=input("enter condition column")
        b=input("enter comparison value")
        d=input("enter new value:")
        cursor.execute("update customer set {}= %s where {}=%s".format(c,a),(d,b))
        con.commit()
        cursor.execute("select*from customer")                  #displaying all records after editing
        rows=cursor.fetchall()
        for i in rows:
            print(i)
            print()
        print("record updated succesfully")
    except Exception as e:
        print(e)

##DEFINING FUNCTION TO DELETE A RECORD
        
def delete_record():
    try:
        delt=int(input("enter the id of the record you wish to delete:"))    #deleting records
        cursor.execute("delete from customer where cust_id={}".format(delt,))
        con.commit()
        print()
        print("record deleted")
        
    except Exception as e:
        print(e)

def displayall():
    try:
        cursor.execute("select*from customer")                 #displaying all records
        rows=cursor.fetchall()
        for i in rows:
            print(i)
            
    except Exception as e:
        print(e)
        
####DEFINING FUNCTION TO DISPLAY ALL RECORDS

def search_user():
    
    try:
        item=int(input("enter the id you want to search"))
        cursor.execute("select* from customer where cust_id={}".format(item,))    # searching a record
        result=cursor.fetchall()
        print(result)
    
    except Exception as e:
        
        print(e)

##DEFINING A FUNCTION TO CREATE CHECK IN TABLE
def create_check_in():
    cr="create table if  not exists check_in(name varchar(50), id int, check_in_time datetime)"
    cursor.execute(cr)
    
##INSERTING INTO CHECK IN TABLE
def check_in():
    print("please verify your details")

    name=input("enter name")
    id1=int(input("enter id"))
    try:
        cursor.execute("select* from cust_personal where id={}".format(id1,))   
        res=cursor.fetchall()
        print(res)
        conf=input("would you like to confirm? y/n")
        if conf=="y" or conf=="Y":
            checkin=input("enter date and time of check in")
            cursor.execute("insert into check_in values('{}','{}','{}')".format(name,id1,checkin))
            con.commit()
            print("record entered")
            print("check in successful")
            print()
            print()
            print("             WELCOME TO SUNSHINE HOTEL          ")
            print()
            print("            WE HOPE YOU ENJOY YOUR STAY         ")
        else:
            print("In case of an issue please report it on the reception")
    except Exception as e:
        print(e)
        print("id not found")
        print()
        print("please reserve a room or book room at the reception desk")


##DEFINING A FUNCTION TO CREATE CHECK IN TABLE

def create_check_out():
    fe="create table if  not exists check_out(name varchar(50), id int, check_out_time datetime,pay varchar(100),rewiews varchar(50))"
    cursor.execute(fe)

##INSERTING INTO CHECK OUT TABLE
def checkout():
    print("please enter your details")

    name=input("enter name")
    id1=int(input("enter id"))
    time=input("enter check-out date and time")
    pay=input("enter your preffered mode of payment")
    w=input("would you like to review us? y/n")
    if w=="y" or w=="Y":
        rew=input("please enter your reviews")
        cursor.execute("insert into check_out values('{}','{}','{}','{}','{}')".format(name, id1, time, pay, rew))
        con.commit()
        print("              THANK YOU FOR YOUR HONEST REVIEW              ")
        print()
        print("              THANK YOU FOR STAYING IN SUNSHINE HOTEL              ")
        print()
        print("              WE HOPE YOU ENJOYED YOUR STAY              ")
        
        print()
        
    else:
        rew="NULL"
        cursor.execute("insert into check_out values('{}','{}','{}','{}','{}')".format(name, id1, time, pay, rew))
        con.commit()

        
        print("              THANK YOU FOR YOUR HONEST REVIEW              ")
        print()
        print("              THANK YOU FOR STAYING IN SUNSHINE HOTEL              ")
        print()
        print("              WE HOPE YOU ENJOYED YOUR STAY              ")

##DEFIINING THE MAIN FUNCTION

def main():
    print("**************************WELCOME TO SUNSHINE HOTEL**************************")
    print("    are you?")
    print('''    1. admin
    2. customer''')
    ch=int(input())
    if ch==1:
        print("    hello user    ")
        print("    please verify    ")
        admin()
##        admin_handle()
        print("THANK YOU ADMIN")
        print()
        print("*******************************************************************************************************************")
        
    elif ch==2:
        print("what would you like to do?")
        print()
        print('''          1. reserve a room

          2. check in
          
          3. check out''')
        print()
        choice1=int(input("enter choice"))
        
        if choice1==1:
            reserve()
        elif choice1==2:
            create_check_in()
            check_in()
        elif choice1==3:
            create_check_out()
            checkout()
        else:
            print("please enter a valid choice")
    else:
        print("please enter a valid choice")
main()
        
        
        
        
    
    
        
    
        
    
        
         
        
     

            




    
    











    
    
    

    
                
    
