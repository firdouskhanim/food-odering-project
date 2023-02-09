import json as js
import admin
class user:
  def __init__(self):
      self.userid=1
      self.detail={}
      self.food={}
  def show(self,name,mobno,email,address,password):
      f=open("user.json","w")
      self.name=name
      self.mobno=mobno
      self.email=email
      self.address=address
      self.password=password
      self.detail[self.userid]=[ name,mobno,email, address,password]       
      js.dump(self.detail,f)
      f.close()
      f=open("user.json")
      r=js.load(f)
      for i,j in r.items():
         print(i,j)
  def log_in(self,name,password):
      f=open("user.json")
      r=js.load(f)
      for i,j in r.items():
       if j[0]==name and j[4]==password:
          print("YOUR ARE LOG IN SUCCESSFULLY ")
          print("****WELCOME TO MY RESTAURANT****")
     
       else:
          print("WRONG ID AND PASSWORD PLEASE TRY AGAIN.")   
       f.close()
  def display(self,option):
      self.option=option
      if option==1:
         print("***** SHOW ORDER*****")
         fh=open("data.json")
         r=js.load(fh)
         for i,j in r.items():
             print(i,j)
         
      if option==2:
         print("*****BOOK ORDER******")  
         fh=open("data.json")
         r=js.load(fh)
         order=input("ENTER THE PLACE ORDER :   ")
         for i,j in r.items():
          if i==order: 
             print(i,j) 
             j[0]=input("ENTER THE ADD FOOD ITEM:    ")
             j[1]=input("ENTER THE  ADD FOOD ITEM PRICE:  ")
             j[2]=int(input("ENTER THE FOOD  OF QUANTITY:  "))
             self.food[i]=[j[0],j[1],j[2]]
          fh=open("order.json","w")
          js.dump(self.food,fh)
          fh.close()
          fh=open("order.json")
          r=js.load(fh)
          for i,j in r.items():
              print(i,j)
      if option==3:
         print("*****ORDER HISTORY*****")
         fh=open("order.json")
         r=js.load(fh)
         for i,j in r.items():
             print(i,j)     
  def update_profile(self,id):
      self.id=id
      f=open("user.json")
      r=js.load(f) 
      for i,j in r.items(): 
       if i==id:
          j[0]=input("ENTER THE FULL NAME:    ")
          j[1]=input("ENTER THE MOBILE NUMBER:   ")
          j[2]=input("ENTER THE EMAIL ID :   ")
          j[3]=input("ENTER THE ADDRESS:    ")
          j[4]=input("ENTER THE PASSWORD:    ")
          self.detail[self.userid]=[j[0],j[1],j[2],j[3],j[4]]       
          f=open("user.json","w")
          js.dump(self.detail,f)
          f.close()
          f=open("user.json")
          r=js.load(f)
          for i,j in r.items():
              print(i,j)