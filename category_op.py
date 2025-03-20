

from flask import render_template,redirect,url_for,request
import mysql.connector
from main import app
from main import app


con = mysql.connector.connect(host= "localhost",username="root" ,password = "sanket07", database = "cake_combo")

cursor = con.cursor()

@app.route("/addcategory",methods=["GET","POST"])
def addcategory():
    if request.method == "GET":
        return render_template("addcategory.html")
    
    else :
        cname = request.form["cname"]
        sql = "insert into category (category_name) values(%s)"
        val = (cname,)
        cursor.execute(sql,val)
        con.commit()
        return redirect(url_for("showallcategories"))
        
@app.route("/showallcategories")
def showallcategories():
    sql = "select * from category"
    cursor.execute(sql)
    cats =cursor.fetchall()
    return render_template("showallcategories.html", cats = cats)



@app.route("/deletecategory/<cid>" ,methods = ["GET","POST"])
def deletecategory(cid):
     if request.method == "GET":
        return render_template("deletecategory.html")
     else :
         action = request.form["action"]
         if action == "Yes":
            #  sql = "delete from category where  Category_name=%s"
             sql = "delete from category where   Category_id= %s"
             val =(cid,)
             cursor.execute(sql,val)
             con.commit()
         return redirect(url_for("showallcategories"))
    

             




@app.route("/editcategory/<cid>" ,methods = ["GET","POST"])
def editcategory(cid):
     if request.method == "GET":
        sql = "select * from category where Category_id=%s"
        val = (cid,)
        cursor.execute(sql,val)
        cat= cursor.fetchone()
        return render_template("editcategory.html ",cat = cat)
     

     else :
        cname = request.form["cname"]
        sql = "update category set Category_name = %s where Category_id =%s"

        val =(cname,cid)
        cursor.execute(sql,val)
        return redirect(url_for("showallcategories"))
