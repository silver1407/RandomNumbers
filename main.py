
'''
#Create an amount of random numbers then add them to a csv file
import random
import csv

#Create a list of random numbers
numbers = []
def random_numbers():
    for i in range(1000):
        numbers.append(random.randint(0, 10))
    return numbers

#Write the list to a csv file
with open('random_numbers.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(numbers)

#Read the csv file and print the numbers
with open('random_numbers.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#Sort the data and display it
numbers.sort()
print(random_numbers)

#Display the average of the data
print(sum(random_numbers)/len(random_numbers))

'''

# Continuous Data
import random
import csv

# Generate 1000 random numbers from 0 to 10 and write the average to csv file 49 times
for i in range(50):
    numbers = []
    for i in range(100):
        numbers.append(random.randint(0, 10))
    with open('random_numbers.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([sum(numbers)/len(numbers)])

# Read the csv file and print the numbers in an array
printarray = []
with open('random_numbers.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row != []:
            printarray.append(row)
        print(row)

# Sort the data and display it
print(printarray)


