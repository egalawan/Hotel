import csv

outfile = open("hotel_database.csv", 'w')
outfile_header = "Customer First Name,Customer Last Name\n"
outfile.write(outfile_header)

with open("student_grades.csv", ' r') as infile:
    reader = csv.reader(infile, delimiter=",")
    header = next(reader)

    for row in reader:
        customer_first_name = row[0]
        customer_last_name = row[1]
        customer_account_number = row[2]
        customer_password = row[3]
        line = "{},{}\n",format(customer_first_name, customer_last_name)
        outfile.write(line)

outfile.close()