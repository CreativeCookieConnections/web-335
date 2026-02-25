"""
Author: Aisha Keller
Date: 02/25/2026
File Name: keller_usersp2.py
Description: Exercise 6.3 Python with MongoDB, Part II - Building a Python program that connects to MongoDB database called web335DB.
"""

# Import the MongoClient
from pymongo import MongoClient
import datetime

# Build a connection string to connect to MongoDB Atlas
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.bfy9zvm.mongodb.net/?retryWrites=true&w=majority")

# Configure a variable to access the web335DB database
db = client['web335DB']

# Create a new user document and add it to the users collection
smith = {
    "firstName": "Joseph",
    "lastName": "Smith",
    "employeeId": "1013",
    "email": "jsmith@me.com",
    "dateCreated": datetime.datetime.utcnow()
}

# Insert the document into the users collection
smith_user_id = db.users.insert_one(smith).inserted_id
print(smith_user_id)

# Prove the insert worked by searching the collection for the document
print(db.users.find_one({"employeeId": "1013"}))

# Update the document by changing the email address
db.users.update_one({"employeeId": "1013"}, {"$set": {"email": "joseph.smith@me.com"}})

# Prove the update worked by searching the collection for the user by employeeId and printing the email address
print(db.users.find_one({"employeeId": "1013"}))

# Build a query to remove a user document
result = db.users.delete_one({"employeeId": "1013"})

# Display the results of the query to prove the document was removed
print(result)

# Prove the delete worked by searching the collection for the document
print(db.users.find_one({"employeeId": "1013"}))