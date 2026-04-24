import streamlit as st
import pymongo
st.title("DATABASE CONNECTIVITY USING MOGODB")
c1,c2=st.columns(2)

myclient = pymongo.MongoClient("mongodb+srv://kunalg15_db_user:UchdhJoflEo7GMli@citcapp.mong26u.mongodb.net/?appName=CitcApp")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
n=c1.text_input("Enter name")
a=c1.text_input("Enter address")
b=c1.button("Save")
if b:
       mydict = { "name":n,"address":a }
       mycol.insert_one(mydict)
       c1.success("Record Save")

n1=c2.text_input("Enter name",key='u')
a1=c2.text_input("Enter address",key='a')
b1=c2.button("Login")
if b1:
     res=mycol.find({"name":n1,"address":a1})
     c2.success(n1)
     c2.success(a1)
     c2.success(res)

    
     for data in res:
             c2.success("Login successfully ")
             c2.success(f"Welcome:{data['name']}")
            
