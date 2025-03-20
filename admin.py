



from flask import render_template,redirect,url_for,request,session
import mysql.connector
from main import app
from main import app
app.secret_key= "Firstbit"


con = mysql.connector.connect(host= "localhost",username="root" ,password = "sanket07", database = "cake_combo")

cursor = con.cursor()


def adminlogin():
    if request.method == "GET":
        return render_template("adminlogin.html")
    
    else :
        uname = request.form["uname"]
        pwd = request.form["pwd"]
        sql = "select count(*) from AdminLogin where username= %s and password = %s"
        val = (uname ,pwd)
        cursor.execute(sql,val)
        count = cursor.fetchone()

        if count[0] ==1 :
            session["uname"] = uname
            return redirect("/adminDashboard")

            # return "Login Succesfull"
        else :
            return redirect(url_for("adminlogin"))
            # return "Login Failed"
        
       
    
def adminlogout():
    session.clear()
    return render_template("adminlogin")


def adminDashboard():
    if "uname" in session:
        return render_template("adminDashboard.html")
    
    else :
        return  redirect(url_for("adminlogin"))



