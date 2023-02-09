import json as js
class admin:
  def __init__(self,name,discount):
      self.name=name 
      self.discount=discount
      self.data={}

  def add_item(self):
      n=int(input("HOW MANY ADD FOOD ITEM:    "))
      for i in range(n):
          foodid=int(input("ENTER THE FOOD ID :"))
          item=input("ENTER THE ADD FOOD ITEM:    ")
          price=input("ENTER THE  ADD FOOD ITEM PRICE:  ")
          qty=int(input("ENTER THE FOOD  OF QUANTITY:  "))
          self.data[foodid]=[item,price,qty,self.discount]
      fh=open("data.json","w")
      js.dump(self.data,fh)
      fh.close()
      fh=open("data.json")
      r=js.load(fh)
      for i,j in r.items():
          print(i,j)
     
  def show(self,foodid):
      self.foodid=foodid
      fh=open("data.json")
      r=js.load(fh)
      for i,j in r.items():
       if foodid==i:
          print("ADMIN NAME :",self.name) 
          print("YOUR ID GENERATE SUCCESSFULLY")
       else: 
          print("WRONG ID  PLEASE TRY AGAIN  ")

  def view_item(self,itemid):
      fh=open("data.json")
      r=js.load(fh)
      for i,j in r.items():
        if itemid==i:
           print(i,j)
         
  def display_food(self):
      fh=open("data.json")
      r=js.load(fh)
      for i,j in r.items():
          print(i,j)

  def remove_item(self,itemid):
      fh=open("data.json")
      r=js.load(fh)
      for i,j in r.items():
        if i==itemid:
           del r[i]
           
      fh=open("data.json","w")
      js.dump(r,fh)
      fh.close()
     