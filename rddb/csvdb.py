import csv
import glob
import os



class CsvDb:
    

################################################################################
#
# Initialise our DB class
#
################################################################################
    
    def __init__(self, db_path):

        """
        
        Constructor. Loads the database from the supplied path

        Returns: void

        Keyword arguments:

        db_path -- the file path to load the DB data from

        """
        
        # set the path
        self.path = db_path

        # load the table data (if any)
        self.loadTables(db_path)


################################################################################
#
# Loads the data from all tables into the Object
#
################################################################################

    def loadTables(self, db_path):

        """
        
        Loads the CSV files from directory <db_path> and creates the database in
        memory

        Returns: void

        Keyword arguments:

        db_path -- the file path to load the DB data from

        """

        # get the list of files
        csv_files = self.getFileList(db_path)

        # set up a dict to hold our table data
        tables = {}
        
        for csv_file in csv_files:
            
            # get the filename without the .csv
            table_name = os.path.basename(csv_file).split('.')[0]

            # add the key / table name to our tables dict and set placeholders
            tables[table_name] = {
                'fields': [],
                'data': [],
            }

            # Create a new CSV reader
            with open(csv_file, newline='') as csvDataFile:
                csvReader = csv.reader(csvDataFile)
                
                i = 0 # set our index to zero
                
                # loop over the rows in our CSV
                for row in csvReader:
                    
                    # check the index
                    if i == 0: 
                        # We've got the header row
                        tables[table_name]['fields'] = [field.lower() for field in row]
                    else:
                        # We have a data row
                        tables[table_name]['data'].append(row)
                    i =+ 1 # increment the index!
            
        self.tables = tables


################################################################################
#
# Gets a list of CSV files in a given directory
#
################################################################################
    
    def getFileList(self, db_path):

        """
        
        Gets a list of all CSV files in the directory <db_path>

        Returns: List of CSV file paths

        Keyword arguments:

        db_path -- the file path to load the DB data from

        """

        # check the directory exists
        if os.path.exists(db_path):

            # get a list of all CSV files in the directory
            csv_files = glob.glob(db_path + '/*.csv')
            
            if len(csv_files) == 0:
                # No files found inside the folder
                raise FileNotFoundError('No table files found in' + db_path)
            
            return csv_files

        else:
            # No directory found containing the database
            raise FileNotFoundError('No database found at ' + db_path)


################################################################################
#
# Loads ALL data from a table
#
################################################################################

    def all(self, table_name):

        """
        
        Loads all rows from a given table <table_name>

        Returns: List of Lists

        Keyword arguments:

        table_name -- the file path to load the DB data from

        """
        
        key_index = self.getKeyIndex(table_name, key)

        target_table = self.tables[table_name]

        for row in target_table['data']:

            if  row[key_index] == value:

                return row
            
        return []


################################################################################
#
# SELECTs data from a table where a column matches a value
#
################################################################################

    def select(self, table_name, key, value):

        """
        
        Searches the table <table_name> for a row where <key> matches <value>

        Returns: List of the data or epty list if no match found

        Keyword arguments:

        table_name -- the table to update
        key -- the key or column name to search over
        value -- the value to search for

        """
        
        key_index = self.getKeyIndex(table_name, key)

        target_table = self.tables[table_name]

        for row in target_table['data']:

            if  row[key_index] == value:

                return row
            
        return []


################################################################################
#
# INSERTs a new row to the specified table
#
################################################################################

    def insert(self, table_name, data):

        """
        
        Adds the row <data> to the table <table_name>

        Returns: True on success

        Keyword arguments:

        table_name -- the table to add data to
        data -- List of values to be added to the table

        """
        
        self.tables[table_name]['data'].append(data)
        
        self.saveTable(table_name)
        
        return True


################################################################################
#
# UPDATEs an item in the specified table
#
################################################################################

    def update(self, table_name, key, value, data):
        """
        
        Update the row in table <table_name> where <key> matches <value> and
        set the data to <data>
        
        Returns: True on sucess or False on failure.

        Keyword arguments:

        table_name -- the table to update
        key -- the key or column name to search over
        value -- the value to search for
        data -- the new data for the row

        """
        
        key_index = self.getKeyIndex(table_name, key)

        target_table = self.tables[table_name]

        row_index = 0

        for row in target_table['data']:

            if  row[key_index] == value:

                self.tables[table_name]['data'][row_index] = data

                self.saveTable(table_name)

                return True

            row_index += 1

        return False    


################################################################################
#
# DELETEs an item from the table <table_name> where <key> matches <value>
#
################################################################################

    def delete(self, table_name, key, value):

        """
        
        Delete an item from the table <table_name> where <key> matches <value>
        and return True on sucess or False on failure.

        Keyword arguments:

        table_name -- the table to update
        key -- the key or column name to search over
        value -- the value to search for

        """

        # Get the key index
        key_index = self.getKeyIndex(table_name, key)

        # Loop over the rows in that table to look for a record where 
        # <key> matches <value>
        for row in self.tables[table_name]['data']:

            if  row[key_index] == value:
                
                # found one!
                # Remove the row
                self.tables[table_name]['data'].remove(row)
                self.saveTable(table_name)
                return True

        return False


################################################################################
#
# Helper methods
#
################################################################################

    def getKeyIndex(self, table_name, key):

        """
        
        Find the list index of <key> in the table <table_name> and 
        
        Returns: the index as an integer

        Keyword arguments:

        table_name -- the table to update
        key -- the key or column name to search for

        """

        return self.tables[table_name]['fields'].index(key.lower())


    
    def saveTable(self, table_name):

        """
        
        Update the CSV file behind the table <table_name> to match the current
        state of the table in memory

        Has no return value

        Keyword arguments:

        table_name -- the table to update

        """

        # Work out the file name
        table_file_path = self.path + '/' + table_name + '.csv'

        # Open the file
        with open(table_file_path, "w", newline="") as f:
            
            # Set up a CSV writer
            writer = csv.writer(f)
            
            # Write the header row
            writer.writerow(self.tables[table_name]['fields'])
            
            # Write the data rows
            writer.writerows(self.tables[table_name]['data'])


# __main__ test
if __name__ == "__main__":
    raise SystemError('Module cannot be called directly')