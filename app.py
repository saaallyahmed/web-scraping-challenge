import os
from flask import Flask, render_template
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    # Run the scrape function
    mars = mongo.db.mars
    Mars_data = scrape_mars.scrape_info()
    print(Mars_data)
    # Update the Mongo database using update and upsert=True
    #mongo.db.collection.update({}, Mars_data, upsert=True)
    mongo.db.collection.update_one({}, {"$set": Mars_data}, upsert=True)

    # Redirect back to home page
    return redirect("/Marsdata")


if __name__ == "__main__":
    app.run(debug=True)