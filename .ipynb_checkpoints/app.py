import os
from flask import Flask, render_template
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo


app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/Marsdata")
def Marsdata():
    # Find one record of data from the mongo database
    Mars_facts_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("Marsdata.html", Mars=Mars_facts_data)


@app.route("/scrape")
def scrape():
    # Run the scrape function
    Mars_data = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, Mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/Marsdata")


if __name__ == "__main__":
    app.run(debug=True)