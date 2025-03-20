# All url configuration will be present here 
from main import app
import category_op as ct
import cake_op as ck
import admin as cp
import user 


#########################  categories #########################
app.add_url_rule("/showallcategories",view_func=ct.showallcategories)
app.add_url_rule("/addcategory",view_func=ct.addcategory,methods=["GET","POST"])

app.add_url_rule("/editcategory/<cid>",view_func=ct.editcategory,methods=["GET","POST"])

app.add_url_rule("/deletecategory/<cid>",view_func=ct.deletecategory,methods=["GET","POST"])


####################### cake ####################################
app.add_url_rule("/showAllCakes",view_func=ck.showAllCakes,methods=["GET","POST"])

app.add_url_rule("/addNewCake",view_func=ck.addNewCake,methods=["GET","POST"])



app.add_url_rule("/deletecake/<cake_id>",view_func=ck.deletecake,methods=["GET","POST"])


app.add_url_rule("/editcake/<cake_id>",view_func=ck.editcake,methods=["GET","POST"])


#######################  admin login ##############################
app.add_url_rule("/adminlogin",view_func=cp.adminlogin,methods=["GET","POST"])


app.add_url_rule("/adminlogout",view_func=cp.adminlogout,methods=["GET","POST"])


app.add_url_rule("/adminDashboard",view_func=cp.adminDashboard,methods=["GET","POST"])



######################### user ####################################

app.add_url_rule("/", view_func=user.homePage )
app.add_url_rule("/ShowCakes/<cat_id>", view_func=user.ShowCakes)
app.add_url_rule("/ViewDetails/<cake_id>", view_func=user.ViewDetails,methods=["GET","POST"])
app.add_url_rule("/Register",view_func=user.Register,methods=["GET","POST"])
app.add_url_rule("/login",view_func=user.login,methods=["GET","POST"])
app.add_url_rule("/logout",view_func=user.logout)
app.add_url_rule("/showcart",view_func=user.showcart,methods=["GET","POST"])