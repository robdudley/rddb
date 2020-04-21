from pprint import pprint 
from rddb import CsvDb

def main():
    # Instantiate our Database
    db = CsvDb('testdb')

    pprint(vars(db))

    # Search for a person called Dave
    person = db.select('people', 'firstname', 'dave')
    print(person)


    new_person = db.insert('people', ['Annie', 'Anderson', 33, 52])
    print(new_person)


    updated_person = db.update('people', 'firstname', 'dave', ['David', 'Davis', 24, 56])
    print(updated_person)

    deleted_person = db.delete('people', 'firstname', 'Anton')
    print(deleted_person)

    pprint(vars(db))



if __name__ == "__main__":
    main()