import csv
# opening and reading csv file
with open('budgetDataHW2.csv') as file:
    # split by new line
    lines = file.read().split("\n")
# setting up a list
num_list = []
for line in lines:
    try:
        # splitting off non numbers
        item = line.split(",")[1][:]
        # appending to the list the number values from line 1
        num_list.append(float(item))
    # if it can't split, will move on
    except:
        pass
# setting these variables to compute later
max_rev = (max(num_list))
min_rev = (min(num_list))

# reading and opening as a whole instead of by line
with open('budgetDataHW2.csv', 'r') as file:
    csv_reader = csv.reader(file)
    # skipping over the header
    next(csv_reader)
    # set these values to 0 so it works correctly in below code
    count = 0
    total_revenue = 0

    # itterating over the csv
    for line in csv_reader:
        # could be any word, this will "happen" for every line in csv_reader
        count = count + 1
        # the integers, aka revenue, in line 1 will be added up
        total_revenue = total_revenue + int(line[1])
# calculating the average change in revenue over time period
avg_change_rev = (max_rev - min_rev)/count

print("Financial Analysis")
print("----------------------------")
print("Total Number of Months: " + str(count))
print("Total Revenue:", total_revenue)
print("Average Change in Revenue:", avg_change_rev)


