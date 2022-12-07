import csv
import os

from employees.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

database_url = 'postgresql://postgres:SFnKiwDN4jaAWaP8zKfE@containers-us-west-78.railway.app:containers-us-west-78.railway.app/railway'
engine = create_engine(os.getenv(database_url))
db = scoped_session(sessionmaker(bind=engine))

def main():
	f = open("employee-list.csv")
	#db.execute("CREATE TABLE IF NOT EXISTS employees_employee (id INTEGER PRIMARY KEY autoincrement, isbn VARCHAR, title VARCHAR, author VARCHAR, year INTEGER")
	reader = csv.reader(f)
    for City, State, Zipcode, Birthday in reader:
        #do
	for Gender, Title, GivenName, MiddleInitial, Surname, City, State, ZipCode, Birthday in reader:
		db.execute("INSERT INTO employees_employee (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)", {"isbn": isbn, "title": title, "author": author, "year": year})
		db.execute("INSERT INTO employees_employee (gender, title, givenName, middleInitial, surname, birthday) VALUES (:isbn, :title, :author, :year)", {"isbn": isbn, "title": title, "author": author, "year": year})
        print(f"added book{title} with ISBN:{isbn} by {author} in {year}")
	db.commit()

if __name__ == "__main__":
	main()