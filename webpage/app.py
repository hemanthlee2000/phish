from flask import Flask, render_template, request
import mysql.connector
import webbrowser
from flask_mysqldb 

app = Flask(__name__)
# Create cursor object
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
         #fetch 
         userDetails = request.form
         name = userDetails['username']
         password = userDetails['password']
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
