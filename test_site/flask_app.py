from flask import Flask, render_template, request, session

from get_shop_data_from_db import get_coffee_shops
from get_user_data_from_db import get_user_data_db

app = Flask(__name__)
print(__name__)

# Add this line for session variables
app.secret_key = 'super_secret_key_20002005'

# route decorator function
# which lives inside app object which is declared in [FLASK class]
@app.route("/")
def index():
    return render_template("index.html", login_status = session.get('is_logged_in', False), user = session.get('user','not'))

@app.route("/<name>/<num>")
def greet(name,num):
    return render_template("greeting.html", age= num, name = name)

@app.route('/findshoptest', methods = ['POST'])
def display_output():
    zip_code = request.form.get('zip')
    shops = get_coffee_shops(filter=zip_code)
    return render_template("index.html" , coffee_shops = shops)

@app.route("/show_login")
def show_login():
    return render_template("index.html", login_status = session.get('is_logged_in', False), show_login_screen=True)

@app.route("/process_login", methods = ['POST'])
def display_user_data():
    user_id= request.form.get('username')
    submitted_password=request.form.get('password')
    user_info=get_user_data_db(filter=user_id)
    actual_password = user_info[0]['password']
    
    if submitted_password == actual_password:
        session['is_logged_in'] = True
        session['user'] = user_id
        session['last_login'] =user_info[0]['last_login']
        show_login = False
        print('successful login')
    else:
        session['is_logged_in'] = False
        session['user'] = "not"
        show_login = True
        print('fail to login')
    return render_template("index.html",user = session.get('user','not'), login_status = session.get('is_logged_in', False), last_login =session.get('last_login', '') ,show_login_screen=show_login)

@app.route("/logout")
def set_logged_out():
    session['is_logged_in'] = False
    session['user'] = "not"
    return render_template("index.html", login_status = session.get('is_logged_in', False), show_login_screen=False)

#Lines below replaces cmd line "flask run"
if __name__ == "__main__":
    app.run(debug=True)

#NOTE: __main__ this is the current file where the code is located