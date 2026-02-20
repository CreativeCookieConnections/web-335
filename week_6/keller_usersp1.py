"""
Author: Aisha Keller
Date: 2/20/2026
File Name: keller_usersp1.py
Description: Exercise 6.3 Python with MongoDB - Building a Python program that connects to your MongoDB database and performs various operations.
"""

# Import the MongoClient
from pymongo import MongoClient
from pprint import pprint

# Connection string from MongoDB Atlas
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.bfy9zvm.mongodb.net/?retryWrites=true&w=majority")

# Connect to the 'web335DB' database
db = client['web335DB']

# Connect to the 'users' collection
users = db['users']

print("Connected to MongoDB Atlas and accessed the 'users' collection.")

# Display all documents in the 'users' collection
print("\n--- Display All Users ---")

for user in users.find():
    pprint(user)

# Display a document where the employeeId is 1011
print("\n--- Display User with employeeId 1011 ---")

employee = users.find_one({"employeeId": "1011"})
pprint(employee)

# Display documents where the last name is "Mozart"
print("\n--- Display Users with last name 'Mozart' ---")

mozart = users.find({"lastName": "Mozart"})
for user in mozart:
    pprint(user)

