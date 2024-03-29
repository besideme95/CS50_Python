import sys
import csv

# main function
def main():
    command_line()
    output = []
    try:
        with open(sys.argv[1], 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                split_name = row['name'].split(',')
                output.append({'first': split_name[1].lstrip(), 'last': split_name[0], 'house': row['house']})

    except FileNotFoundError:
        print(f'Could not read {sys.argv[1]}')

    with open(sys.argv[2], 'w') as file:
        writer = csv.DictWriter(file, fieldnames= ['first','last','house'])
        writer.writerow({'first': 'first', 'last': 'last', 'house': 'house'})
        for row in output:
            writer.writerow({'first': row['first'], 'last': row['last'], 'house':row['house']})


# command line
def command_line():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    if '.csv' not in sys.argv[1] or '.csv' not in sys.argv[2]:
        sys.exit('Not a CSV file')

if __name__ == "__main__":
    main()
