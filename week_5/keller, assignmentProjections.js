/*
Author: Aisha Keller
Date: 02/10/2026
File: keller_assignmentProjections.js
Description: MongoDB Exercise queries with projections in Mongo Shell
*/

/**
 * a) Add a new user to the users collection.
 * Insert a new document using the same fields as existing user documents.
 * Providing proof the insert succeeded by finding the inserted document.
 */

// Insert a new user document into the users collection
db.users.insertOne({
    firstName: "George",
    lastName: "Handel",
    employeeId: "1013",
    email: "ghandel@me.com",
    dateCreated: new Date()
});

// Prove the new user was added
db.users.find(
    { email: "ghandel@me.com" },
);

/**
 * b) Update Mozart's email address to mozart@me.com.
 * Then prove the update succeeded by displaying the updated document.
 */

// Update Mozart's email address
db.users.updateOne(
    { lastName: "Mozart" },
    { $set: { email: "mozart@me.com" } }
);

// Prove the update succeeded
db.users.find(
    { lastName: "Mozart" },
);

/**
 * c) Display all users using projections
 * This returns all documents but only shows firstName, lastName, and email fields.
 * (_id is excluded for clearer output)
 * This is useful for focusing on specific fields and improving readability.
 */

// Display all users with projections for specific fields
db.users.find(
    {},
    {_id: 0, firstName: 1, lastName: 1, email: 1}

);