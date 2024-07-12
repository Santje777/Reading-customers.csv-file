import csv

with open('customers.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
    id = lines[0]
    first_name = lines[2]
    last_name = lines[3]
    email = lines[9]
    
    print(f" Customer #{id}, {first_name} {last_name}, {email}")