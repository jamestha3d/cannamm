import csv
import datetime
#from employees.models import Employee, City
def main():
    f = open("employee-list.csv")
    reader = csv.reader(f)
    counter = 0
    for Gender, Title, GivenName, MiddleInitial, Surname, City, State, ZipCode, Birthday in reader:
        if counter == 0:
            counter += 1
            continue
        birthday = Birthday.split("/")
        bday = datetime.date(int(birthday[2]), int(birthday[0]), int(birthday[1]))
        print(bday)
    

if __name__ == "__main__":
	main()