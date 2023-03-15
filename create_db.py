"""--------------------ι𝐍Ⓙย𝐬𝓣ᶤςⒺ Ⓐ𝐍ＹωᕼⒺг𝐄 ᶤ𝐬 ᵃ tｈяᗴＡт ⓉＯ 𝐣υ𝔰ｔ𝐢ᶜⓔ 𝐄V乇яｙ山卄εŘ乇 --------------------
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
--------------------ι𝐍Ⓙย𝐬𝓣ᶤςⒺ Ⓐ𝐍ＹωᕼⒺг𝐄 ᶤ𝐬 ᵃ tｈяᗴＡт ⓉＯ 𝐣υ𝔰ｔ𝐢ᶜⓔ 𝐄V乇яｙ山卄εŘ乇 --------------------"""
import os, inspect, sqlite3, datetime
from faker import Faker
from datetime import datetime

def main():
    global db_path
    db_path = os.path.join(get_script_dir(), 'social_network.db')
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # Open a connection to the database.
    con = sqlite3.connect('social_network.db')
    # Get a Cursor object that can be used to run SQL queries on the database.
    cur = con.cursor()
    # Define an SQL query that creates a table named 'people'.
    # Each row in this table will hold information about a specific person.
    create_ppl_tbl_query = """
    CREATE TABLE IF NOT EXISTS people
    (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    province TEXT NOT NULL,
    bio TEXT,
    age INTEGER,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
    );
    """
    # Execute the SQL query to create the 'people' table.
    # Database operations like this are called transactions.
    cur.execute(create_ppl_tbl_query)
    # Commit (save) pending transactions to the database.
    # Transactions must be committed to be persistent.
    con.commit()
    # Close the database connection.
    # Pending transactions are not implicitly committed, so any
    # pending transactions that have not been committed will be lost.
    con.close()

def populate_people_table():
    """Populates the people table with 200 fake people"""
    fake = Faker('en_CA')
    fake_us = Faker('en_US')
    # Open connection to DB.
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    # Define an SQL query that inserts a row of data in the people table.
    # The ?'s are placeholders to be fill in when the query is executed.
    # Specific values can be passed as a tuple into the execute() method.
    add_person_query = """
    INSERT INTO people
            (
            name,
            email,
            address,
            city,
            province,
            bio,
            age,
            created_at,
            updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    # Define a tuple of data for the new person to insert into people table.
    for new_person in range(200):
        new_person = (
            fake.first_name(),
            fake.ascii_email(),
            fake.street_address(),
            fake.city(),
            fake.administrative_unit(),
            fake_us.sentence(nb_words=10),
            fake.random_int(min=1, max=100),
            datetime.now().strftime('%c'),
            datetime.now().strftime('%c'))
        # Execute query to add new person to people table.
        cur.execute(add_person_query, new_person)
        con.commit()
    con.close()

def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

if __name__ == '__main__':
   main()