import csv

namefile = 'file/file_02.csv'
file = open(namefile)
data = csv.reader(file, delimiter=',')

# print(data)

for item in data:
    print(item)