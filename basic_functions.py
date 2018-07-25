"""
Author : Parag

Purpose : Program for understanding basic operations of MySQL database

Operations performed on single table - 'accounts'from Database - 'BANK'
operations performed =
1) Display all entries from table
2) Add new Entry to table
3) Delete Entry from table
4) Serach and display particulaer entry from table
5) Modify Entry fin table


Before running the program, A database - "BANK" is created using mySQL
a table - "accounts" is created in the database with 5 columns
5 columns are = accnt_no, first_name, last_name, phone_no, balance

use following command in Mysql to create a table
    Mysql    > create table accounts(
        -> accnt_no INT NOT NULL AUTO_INCREMENT,
        -> first_name VARCHAR(40) NOT NULL,
        -> last_name VARCHAR(40) NOT NULL,
        -> phone_no INT,
        -> PRIMARY KEY(accnt_no)
        -> );

"""
import MySQLdb


def display(db):
    print("\n....Printing all data from Database....")

    cursor = db.cursor()

    sql = "SELECT * FROM accounts"

    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            accntno = row[0]
            fname = row[1]
            lname = row[2]
            phn = row[3]
            balance = row[4]
            # Now print fetched result
            print "Account no. = %d, fname = %s,lname = %s,phone no. = %d, balance = %d" % \
                  (accntno, fname, lname, phn, balance)
    except:
        print "Error: unable to display data"


def add_entry(db):
    print("\n....Adding Entry....")

    first_name = raw_input('Enter first name = ')
    Last_name = raw_input('Enter last name = ')
    phone_no = int(raw_input('Enter Phone number = '))

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO accounts(first_name, last_name, phone_no, balance) VALUES ('%s', '%s', '%d', 0)" % \
          (first_name, Last_name, phone_no)

    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        print("Error: Unable to insert into Table")
        db.rollback()


def delete_entry(db):
    print("\n....Deleting Entry....")
    accnt = int(raw_input('Enter account number to be searched = '))
    cursor = db.cursor()

    sql = "DELETE FROM accounts WHERE accnt_no = '%d'" % (accnt)

    try:
        cursor.execute(sql)
        db.commit()

    except:
        print("Error: Unable to delete entry")
        db.rollback()


def serach(db):
    print('\n....Searching....')

    accnt = int(raw_input('Enter account number to be searched = '))
    cursor = db.cursor()

    sql = "SELECT * FROM accounts WHERE accnt_no = '%d'" % (accnt)

    try:
        cursor.execute(sql)
        results = cursor.fetchall()

        # if entry is not found in database above call with return empty object ()
        if results is ():
            print("NO such entry found in database")
        else:
            for row in results:
                accntno = row[0]
                fname = row[1]
                lname = row[2]
                phn = row[3]
                balance = row[4]
                # Now print fetched result
                print "Account no. = %d, fname = %s,lname = %s,phone no. = %d, balance = %d" % \
                      (accntno, fname, lname, phn, balance)
    except:
        print("error in searching")
        db.rollback()


# Function to modify one of the field i.e. we are modifying only phone number here
def modify_entry(db):
    print('\n....Modifying Entry....')
    cursor = db.cursor()

    accnt = int(raw_input('Enter account number to be modified = '))
    phn = int(raw_input('Enter New phone number = '))

    sql = "UPDATE accounts SET phone_no = '%d' WHERE accnt_no = '%d'" % (phn, accnt)

    try:
        cursor.execute(sql)
        db.commit()

    except:
        print("Error: Unable to update entry")
        db.rollback()


def main():
    # Open database connection with following information
    # ip address = localhost
    # User name = root , User password = admin, database name = 'BANK'

    db = MySQLdb.connect("localhost", "root", "admin", "BANK")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print "Database version : %s " % data

    while 1:
        print("\n******MENU*******\n1.Display database \n2.Add entry to database \n3.Delete entry from database \n4.Search Entry \n5.Modify Entry\n6.exit")
        selection = input('Enter your option = ')

        if selection == '1' or selection == 1:
            display(db)
        elif selection == '2' or selection == 2:
            add_entry(db)
        elif selection == '3' or selection == 3:
            delete_entry(db)
        elif selection == '4' or selection == 4:
            serach(db)
        elif selection == '5' or selection == 5:
            modify_entry(db)
        else:
            break

    print("Exiting program")
    # disconnect from server
    db.close()


if __name__ == "__main__":
    main()






