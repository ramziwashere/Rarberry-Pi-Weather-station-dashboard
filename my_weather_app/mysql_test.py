import mysql.connector

try:
    # Connect to the RDS MySQL database
    db = mysql.connector.connect(
        host="mydatabase.cvu00ge8qbju.ap-southeast-2.rds.amazonaws.com",
        user="admin",
        password="password",
        database="mydatabase"
    )
    cursor = db.cursor()

    # Exacute Query for tables
    cursor.execute("SELECT * FROM weather_data ")
    
    tables = cursor.fetchall()
    for i in tables:
        print(i)
    

    # Close the database connection
    db.close()



except mysql.connector.Error as err:
    # Print error message if connection fails
    print("Error:", err)

    
