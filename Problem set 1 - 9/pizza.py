
import sys
import csv
import tabulate as tabulate

#main function
def main():
    check_command_line()

    #table to store the data
    data = []
    #open the file
    try:
        with open(sys.argv[1], 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                data.append(row)
    #If it is not a csv file
    except FileNotFoundError:
        sys.exit('File does not exist')

    #print the table
    print(tabulate.tabulate(data[1:], headers = data[0], tablefmt = 'grid'))

#check the in line command
def check_command_line():
    #if it is too short <2
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    #if it is too long>2
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    #check if it is a csv file
    if '.csv' not in sys.argv[1]:
        sys.exit('Not a CSV file')

if __name__ == '__main__':
    main()
