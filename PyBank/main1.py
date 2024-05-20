import os
import csv

#Initiating the path to the CSV file. 
cwd = os.path.dirname(os.path.abspath(__file__))
csvpath = os.path.join(cwd, "Resources", "budget_data.csv")
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Calculating the number of months 
    value = 0

    #Removing the header row
    next(csvreader)

    #Creating a loop to add all the values to get number of rows or total number of months
    for row in csvreader:
        value += 1

    #Printing the desired output with correct spaces and characters to match the given answer. 
    print("\nFinancial Analysis\n")
    print("-------------------------------------")
    print(f"\nTotal Months : {value}\n")

    text = ("\nFinancial Analysis\n")
    text += ("-------------------------------------")
    text += (f"\nTotal Months : {value}\n")


cwd = os.path.dirname(os.path.abspath(__file__))
csvpath = os.path.join(cwd, "Resources", "budget_data.csv")
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")  

    #Calculating the net total amount of Profit/Losses over entire period
    total_amount = 0
    next(csvreader)

    #Looping through the second column values and adding them to total_amount
    for total in csvreader:
        number = int(total[1])
        total_amount += number
    print(f"Total : ${total_amount}\n")
    text += (f"Total : ${total_amount}\n")


cwd = os.path.dirname(os.path.abspath(__file__))
csvpath = os.path.join(cwd, "Resources", "budget_data.csv")
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)
    
     #Setting the varibles
    values = []
    changes = []

    #Looping thourgh to get each value
    for row in csvreader:
        value = float(row[1])
        values.append(value)
    
    #Calculating changes
    for i in range(1, len(values)):
        change = values[i] - values[i-1]
        changes.append(change)
    
    #Calculating the average
    average_change = sum(changes) / len(changes)

    print(f"Average Changes : ${average_change:.2f}") #:.2f to print answer for 2 decimal points
    text += (f"Average Changes : ${average_change:.2f}")

cwd = os.path.dirname(os.path.abspath(__file__))
csvpath = os.path.join(cwd, "Resources", "budget_data.csv")
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    #Declaring the variables, we need 2 lists one for the dates and one for the changes in Profit/Losses
    date_value = []
    change1 =  []

    #Looping through the date column to get the list of dates storing the dates in date_value
    for row in csvreader:
        date = row[0]
        date_value.append(date)
    
    #Looping through all values to create the list of the change in Proft/Losses from the previous month storing in change1
    for i in range(0, len(changes)):
        change =values[i] - values[i-1]
        change1.append(change)

    #Creating a varible to store the Max and Min values in change1
    max = max(change1)
    min = min(change1)

    #Indexing the values and getting the corresponding dates for the Max and Min values
    max_index = change1.index(max)
    min_index = change1.index(min)
    
    max_date = date_value[max_index]
    min_date = date_value[min_index]
    
    print(f"\nGreatest Increase in Profits: {max_date} (${max})\n")
    print(f"Greatest Decrease in Profits: {min_date} (${min})\n")
    text += (f"\nGreatest Increase in Profits: {max_date} (${max})\n")
    text += (f"Greatest Decrease in Profits: {min_date} (${min})\n")

#Creating an output text file

cwd = os.path.dirname(os.path.abspath(__file__))
csvpath = os.path.join(cwd, "Analysis", "output.txt")
with open(csvpath, "w") as file:
    file.write(text)
print("Output file 'output.txt' created successfully!")





 

    


