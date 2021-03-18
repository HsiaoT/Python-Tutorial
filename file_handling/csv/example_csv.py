
# touch.csv
# echo "1,2,3,4\n5,6,7,8\n9,10,11,12" >> test.csv 

# cat test.csv
# 1,2,3,4
# 5,6,7,8
# 9,10,11,12

import csv

f = open("test.csv","r")
reader = csv.reader(f)
for row in reader:
	for e in row:
		print(e)

print("\n ================== \n")

with open("test.csv") as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print(row)
# ['1', '2', '3', '4']
# ['5', '6', '7', '8']
# ['9', '10', '11', '12']

print("\n ================== \n")

with open("test.csv") as csvfile:
	reader = csv.reader(csvfile, delimiter=" ", quotechar="|")
	for row in reader:
		print(row)
# ['1,2,3,4']
# ['5,6,7,8']
# ['9,10,11,12']

print("\n ================== \n")

with open("test.csv") as csvfile:
	reader = csv.reader(csvfile, delimiter=" ", quotechar="|")
	for row in reader:
		print(",".join(row))
# 1,2,3,4
# 5,6,7,8
# 9,10,11,12

