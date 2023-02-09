import admin
import user
import sys
while True:
      print("[1.] ADMIN [2.] USER")
      choice=int(input("ENTER THE LOGIN FOR ADMIN AND USER"))
      if choice==1:
         obj=admin("ARSHI",5)
         print("[1.] ADD FOOD ITEM \n[2.] LOGIN ID \n[3.] SEARCH MENU USING FOODID \n[4.] SHOW MENU \n[5.] REMOVE ITEM")
         select=int(input("ENTER YOUR CHOICE:    "))
         if select==1:
            obj.add_item() 

         if select==2:
            id=input("ENTER THE FOOD ID TO THE LOGIN ADMIN: ")
            obj.show(id)
      
         if select==3:   
            n=input("ENTER THE SEARCH FOOD ITEM ID:   ")
            obj.view_item(n)

         if select==4:
            print("SHOW THE MENU")
            obj.display_food()
  
         if select==5:
            id=int(input("ARE YOU WANT TO DELETE ITEM IN MENU:   "))
            obj.remove_item(id)
            print("SUCCESSFULLY DELETE IN MENU")  
      if choice==2:
         obj1=user()
         print("[1.] REGISTER APPLICATION FORM \n[2.] LOG IN APPLICATION \n[3.] USER DEFINE FACILITY \n[4.] UPDATE PROFILE")
         ch=int(input ("ENTER THE  USER CHOICE:  "))
         if ch==1:
            print("THE USER CAN REGISTER IN APPLICATION")
            a=input("ENTER THE FULL NAME:    ")
            b=input("ENTER THE MOBILE NUMBER:   ")
            c=input("ENTER THE EMAIL ID :   ")
            d=input("ENTER THE ADDRESS:    ")
            e=input("ENTER THE PASSWORD:    ")
            obj1.show(a,b,c,d,e)

         if ch==2:
            a=input("ENTER THE NAME FOR LOG IN:  ")
            b=input("ENTER THE PASSWORD:     ") 
            obj1.log_in(a,b)  

         if ch==3:
            option=int(input("[1.] SHOW ORDER \n[2.] PLACE NEW ORDER \n[3.] ORDER HISTORY  \nENTER YOUR CHOICE:     "))   
            obj1.display(option)      

         if ch==4: 
            k=input("ENTER THE USER ID :")
            obj1.update_profile(k)
            sys.exit()