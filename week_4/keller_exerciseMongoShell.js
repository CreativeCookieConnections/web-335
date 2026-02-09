/*
Author: Aisha Keller
Date: 02/08/2026
File: keller_exerciseMongoShell.js
Description: MongoDB Exercise queries in Mongo Shell
*/

// Query a: Display all users in the users collection.
db.users.find({});

// Query b: Display the user whose email address is "jbach@me.com"
db.users.find({ email: "jbach@me.com"});

// Query c: Display the user whose last name is "Mozart"
db.users.find({ lastName: "Mozart" });

// Query d: Display the user whose first name is "Richard"
db.users.find({ firstName: "Richard" });

// Query e: Display the user whose employeeId is "1010"
db.users.find({ employeeId: "1010" });
