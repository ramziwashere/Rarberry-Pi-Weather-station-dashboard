from flask import Blueprint, render_template
from flask_login import login_required,current_user

import mysql.connector
from flask import Flask, render_template

import time #added


views = Blueprint('views',__name__)

@views.route('/')
@login_required
def home():
    
     # Connect to the RDS MySQL database
    db = mysql.connector.connect(
        host="mydatabase.cvu00ge8qbju.ap-southeast-2.rds.amazonaws.com",
        user="admin",
        password="password",
        database="mydatabase"
    )
    cursor = db.cursor()

    sql = "SELECT * FROM weather_data WHERE id = (SELECT MAX(id) FROM weather_data)"


    # Execute the SQL query to retrieve all entries from the weather_data table
    cursor.execute(sql)

    # Fetch all entries from the table
    all_entries = cursor.fetchall()

    # Retrieve the last entry from the fetched entries
    last_entry = all_entries

    # Close the database connection
    cursor.close()
    db.close()

    return render_template("home.html", user= current_user, rain_forecast = last_entry[0][8],current_rainfall = last_entry[0][3],current_wind_dir= last_entry[0][7], current_temperature = last_entry[0][2], current_humidity = last_entry[0][5], current_wind =last_entry[0][4])


