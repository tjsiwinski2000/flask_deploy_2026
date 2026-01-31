from flask import Flask, render_template, request
#OLD->text file -> from coffee_shops import shops
from get_data_from_database import get_coffee_shops


app = Flask(__name__)
print(__name__)


# route decorator function
# which lives inside app object which is declared in [FLASK class]
@app.route("/")
def index():
    return render_template("index.html")

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