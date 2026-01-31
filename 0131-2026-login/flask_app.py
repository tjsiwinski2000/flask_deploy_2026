from flask import Flask, render_template, request, session
#✅ONE. get user_data_from file
from get_user_data_from_db import get_user_data_file
#✅TWO. filter user_data from form submit
#THREE. display user_daa on index.html
#FOUR. replace file with sqlite DB
#✅FIVE. make form password hidden char with (*)(*) option
#SIX. make everything modular for transition to PROD site
#SEVEN migrate to PROD


app = Flask(__name__)

# Add this line!
app.secret_key = 'super_secret_key_20002005'

print(__name__)


# route decorator function
# which lives inside app object which is declared in [FLASK class]
@app.route("/")
def index():
     return render_template("index.html", status = session.get('is_logged_in', False))
 
@app.route("/logout")
def set_logged_out():
    session['is_logged_in'] = False
    session['user'] = "not"
    return render_template("index.html", status = session.get('is_logged_in', False))

@app.route("/", methods = ['POST'])
def display_user_data():
    user_id= request.form.get('username')
    submitted_password=request.form.get('password')
    actual_password=get_user_data_file(user_id)
    if submitted_password == actual_password:
        session['is_logged_in'] = True
        session['user'] = user_id
        print('successful login')
    else:
        session['is_logged_in'] = False
        session['user'] = "not"
        print('fail to login')
    return render_template("index.html",user = session['user'], status = session.get('is_logged_in', False))
    #1240pm set form action to post back to index.html 
    

@app.route("/<name>/<num>")
def greet(name,num):
    return render_template("greeting.html", age= num, name = name)

@app.route('/findshoptest', methods = ['POST'])
def display_output():
    zip_code = request.form.get('zip')
    shops = get_coffee_shops(filter=zip_code)
    return render_template("index.html" , coffee_shops = shops)

#Lines below replaces cmd line "flask run"
if __name__ == "__main__":
    app.run(debug=True)

#NOTE: __main__ this is the current file where the code is located