import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    host="mydatabase.cvu00ge8qbju.ap-southeast-2.rds.amazonaws.com",
    user="admin",
    password="password",
    database="mydatabase"
)
# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Define the SQL query to create the weather_data table
create_table_query = """
CREATE TABLE IF NOT EXISTS weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Date DATE,
    Temperature FLOAT,
    Rainfall FLOAT,
    Wind FLOAT,
    Humidity FLOAT,
    Pressure FLOAT,
    Wind_Direction VARCHAR(50),
    Rain_Tomorrow FLOAT
);
"""

# Execute the SQL query to create the table
cursor.execute(create_table_query)

# Commit the transaction
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

print("Table weather_data created successfully")