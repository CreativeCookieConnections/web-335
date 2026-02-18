/*
Author: Aisha Keller
Date: 02/18/2026
File: keller_assignment6.js
Description: Performing various operations on houses and student's collections using MongoDB Shell.
*/

// a. Query to Display all students in the students collection.
db.users.aggregate([
    { $match: {} }
])

// b. Add a new student. Ensure the fields in the new document match the existing fields in the collection.
db.students.insertOne({
    firstName: "Harry",
    lastName: "Potter",
    studentId: "s1001",
    houseId: "h1007"
})  

db.students.aggregate([
    { $match: { studentId: "s1001" } }
])

// c. Update a property from the student previously added in step b. Update the studentId.
db.students.updateOne(
    { studentId: "s1001" },
    { $set: { studentId: "s1002" } }
)

db.students.aggregate([
    { $match: { studentId: "s1002" } }
])


// d. Delete the student added in step b.
db.students.deleteOne(
    { studentId: "s1002" }
)

db.students.aggregate([
    { $match: { studentId: "s1002" } }
])

// e. Display all students by house. Display the house and then the students.
db.houses.aggregate([
    {
        $lookup: {
            from: "students",
            localField: "houseId",
            foreignField: "houseId",
            as: "students"
        }
    }
])


// f. Display all students in house Gryffindor. The order in MongoDB should showcase the house first and then the students.
db.houses.aggregate([
    { $match: { houseId: "h1007" } },
    {
        $lookup: {
            from: "students",
            localField: "houseId",
            foreignField: "houseId",
            as: "students"
        }
    }
])

// g. Display all students in the house with an Eagle mascot. The order should be: House first and then the students.
db.houses.aggregate([
    { $match: { mascot: "Eagle" } },
    {
        $lookup: {
            from: "students",
            localField: "houseId",
            foreignField: "houseId",
            as: "students"
        }
    }
])