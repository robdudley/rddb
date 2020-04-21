from pprint import pprint 
from rddb import CsvDb


# Instantiate our Database with the path to the data / CSV files
db = CsvDb('testdb')


# Print the database before 
pprint(vars(db))


# Search for a person called Dave
person = db.select('people', 'firstname', 'Dave')
pprint(person)


# Add a person to the table
new_person = db.insert('people', ['Annie', 'Anderson', 33, 52])
pprint(new_person)


# Update a person who's last name is Smith 
updated_person = db.update('people', 'lastname', 'Smith', ['Sally', 'Smith', 30, 64])
pprint(updated_person)


# Delete a person who is  Anton
deleted_person = db.delete('people', 'age', 56)
pprint(deleted_person)


# print the database after
pprint(vars(db))
