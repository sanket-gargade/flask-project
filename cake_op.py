from flask import render_template,request,redirect,url_for
import mysql.connector
from werkzeug.utils import secure_filename

def addNewCake():
    con = mysql.connector.connect(host="localhost",user="root",password="sanket07",database="cake_combo")

    cursor = con.cursor()
    if request.method == "GET":
        sql = "select * from category"                
        cursor.execute(sql)
        cats = cursor.fetchall()
        return render_template("addNewCake.html",cats=cats)
    else:
        cname = request.form["cname"]
        price = request.form["price"]
        desc = request.form["description_cake"]        
        cid = request.form["cat_id"]
        f = request.files['image_url'] 
        filename = secure_filename(f.filename)
        filename = "static/images/"+f.filename
        #This will upload / save the file to the specified location
        f.save(filename)   
        filename = "images/"+f.filename        
        con = mysql.connector.connect(host="localhost",user="root",password="sanket07",database="cake_combo")
        sql = "insert into cake(cake_name,price,description_cake,image_url,cat_id) values (%s,%s,%s,%s,%s)"
        val = (cname,price,desc,filename,cid)
        cursor = con.cursor()
        cursor.execute(sql,val)
        con.commit()        
        return redirect(url_for('showAllCakes'))
    


def showAllCakes():
    con = mysql.connector.connect(host="localhost",user="root",password="sanket07",database="cake_combo")
  
    # sql = "select c.cake_id,c.cake_name,c.price,c.description_Cake,c.image_url,c.cat_id,t.cid, from cake c inner join category t on c.cat_id = t.cid"
    sql =  "select * from Cake_Category"
   
    
    cursor = con.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    con.close()
    return render_template("showAllCakes.html",cakes  = result)



def deletecake(cake_id):
     con = mysql.connector.connect(host="localhost",user="root",password="sanket07",database="cake_combo")
     cursor = con.cursor() 


     if request.method == "GET":
        return render_template("deletecake.html")
     else :
         
         action = request.form["action"]
         if action == "Yes":
            #  sql = "delete from category where  Category_name=%s"
             sql = "delete from cake where cake_id= %s"
             val =(cake_id,)
             cursor.execute(sql,val)
             
         return redirect(url_for("showAllCakes"))




def editcake(cake_id):
     con = mysql.connector.connect(host="localhost",user="root",password="sanket07",database="cake_combo")
     cursor = con.cursor() 
     if request.method == "GET":
        sql = "select * from cake where Cake_id=%s"
        val = (cake_id,)
        cursor.execute(sql,val)
        cat= cursor.fetchone()
        return render_template("editcake.html ",cat = cat)
     

     else :
        cname = request.form["cname"]
        sql = "update category set Category_name = %s where Category_id =%s"

        val =(cname,cake_id)
        cursor.execute(sql,val)
        con.commit()
        return redirect(url_for("showAllCakes"))




    


















