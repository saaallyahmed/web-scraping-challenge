from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# @TODO: setup mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# @TODO: write a statement that finds all the items in the db and sets it to a variable
@app.route('/')
def index():
    # Find one record of data from the mongo database
    mars = mongo.db.mars.find_one()
    # Return template and data
    return render_template("index.html", mars=mars)

@app.route('/scrape')
def scrape():
    

if __name__ == "__main__":
    app.run(debug=True)