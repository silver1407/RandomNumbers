#Create an amount of random numbers then add them to a csv file
import random
import csv

#Create a list of random numbers
random_numbers = []
for i in range(49):
    random_numbers.append(random.randint(0, 10))

#Write the list to a csv file
with open('random_numbers.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(random_numbers)

#Read the csv file and print the numbers
with open('random_numbers.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#Sort the data and display it
random_numbers.sort()
print(random_numbers)

#Display the average of the data
print(sum(random_numbers)/len(random_numbers))
