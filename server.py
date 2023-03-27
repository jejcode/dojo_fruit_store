from flask import Flask, render_template, request, redirect
app = Flask(__name__)  
from datetime import datetime

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    # calculate item count before sending it to the page
    total_items = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    current_date = datetime.now()
    date = current_date.strftime("%B %d %Y %I:%M:%S %p")
    print(f"Charging {request.form['first_name']} for {total_items} fruit.")
    # sends form data to the web page. Probably not a good idea, but it works for the assignment
    return render_template("checkout.html", data = request.form, total_items = total_items, date = date)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True, port = 8000)    