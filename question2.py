'''
Create a form on the frontend that, when submitted, inserts data into MongoDB Atlas. Upon successful submission, the user should be redirected to another page displaying the message "Data submitted successfully".
If there's an error during submission, display the error on the same page without redirection.
'''
from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = Flask(__name__)
app.secret_key = "super_secret_key"

# MongoDB Atlas connection setup
MONGO_URI = "mongodb+srv://wobece6207:eGL7TgW3ZOV6N3Ci@cluster0.nygjpwz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

try:
    client = MongoClient(MONGO_URI)
    # Test connection
    client.admin.command('ping')
    print("MongoDB connection successful")
    db = client['user_database']
    collection = db['user_data']
except PyMongoError as e:
    print(f"MongoDB connection error: {str(e)}")

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        # Validate fields
        if not name or not email:
            flash("Name and Email are required.")
            return render_template("form.html")

        try:
            # Insert into MongoDB
            collection.insert_one({"name": name, "email": email})
            return redirect(url_for("success"))
        except PyMongoError as e:
            flash(f"Database Error: {str(e)}")
            return render_template("form.html")

    return render_template("form.html")

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
