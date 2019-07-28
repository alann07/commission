import csv

def main():
    with open('commissions.tsv') as tsvfile:
        reader = csv.DictReader(tsvfile, dialect='excel-tab', delimiter='|')
        for row in reader:
            print(row)


if __name__ == '__main__':
    main()