from flask import   render_template,request,redirect,url_for,session
from main import app
import mysql.connector
con = mysql.connector.connect(host="localhost",user="root",password="sanket07",database="cake_combo")

cursor = con.cursor()

def homePage():
    sql = "select * from category"
    cursor = con.cursor(sql)
    cursor.execute(sql)
    cats = cursor.fetchall()
    sql = "select * from cake_category"
    cursor = con.cursor()
    cursor.execute(sql)
    cakes = cursor.fetchall()
    return render_template("homepage.html",cats=cats,cakes=cakes)


def ShowCakes(cat_id):
    sql = "select * from category"
    cursor = con.cursor()
    cursor.execute(sql)
    cats = cursor.fetchall()
    sql = "select * from cake where cat_id=%s"
    val = (cat_id,)
    cursor = con.cursor()
    cursor.execute(sql ,val)
    cakes = cursor.fetchall()
    return render_template("homepage.html",cats=cats,cakes=cakes)  
    
def ViewDetails(cake_id): 
       
  if request.method == "GET":
    sql = "select * from category"
    cursor = con.cursor()
    cursor.execute(sql)
    cats = cursor.fetchall()
    sql = "select * from cake_category where cake_id=%s"
    val = (cake_id,)
    cursor = con.cursor()
    cursor.execute(sql ,val)
    cake = cursor.fetchone()
    return render_template("ViewDetails.html",cats=cats,cake=cake)
  else:
                                    
        if "username" in session: #User has logged in
            cake_id = request.form["cake_id"]
            sql = "select count(*) from MyCart where cake_id=%s and username=%s"
            val = (cake_id,session["username"])
            cursor = con.cursor()
            cursor.execute(sql,val)
            count = cursor.fetchone()
            count = count[0]
            if count == 1:
               return "Item already in cart"
            #Perform add to cart
            else:
                qty = request.form["qty"]
                sql = "insert into MyCart  (cake_id,username,qty) values (%s,%s,%s)"
                val = (cake_id,session["username"],qty)
                cursor = con.cursor()
                cursor.execute(sql,val)
                con.commit()
                return "Item added to cart"

        else: #User needs to login
            return redirect(url_for("login"))
        

def showcart():
    if request.method == "GET":
        sql = "select * from mycart_details_vw where username=%s"
        val  = (session["username"],)
        cursor = con.cursor()
        cursor.execute(sql,val)
        items = cursor.fetchall()
        return render_template("showcart.html",items=items)
    
    else:
        pass

    
       
          
  
  



def Register():
    if request.method == "GET":
        return render_template("Register.html")
    
    else :
        username = request.form["uname"]
        password = request.form["pwd"]
        try:
          sql = "insert into user_info values (%s,%s)"
          val = (username,password)
          cursor = con.cursor()
          cursor.execute(sql,val)
          con.commit()
          "User Added.."

        except:
            return "Duplicate user"
        else:
            return "User added"
    

def login():
    if request.method == "GET":
        return render_template("Login.html")
    
    else:
        username = request.form["uname"]
        password = request.form["pwd"]
        sql = "select count(*) from user_info where username=%s and password=%s"
        val = (username,password)
        cursor = con.cursor()
        cursor.execute(sql,val)
        count = cursor.fetchone()
        count = count[0]

        if count == 1:
            session["username"] = username
            return redirect(url_for("homePage"))
        
        else:
            return  redirect(url_for("login"))


def logout ():
    session.clear()
    return redirect(url_for("homePage"))




      



      


   