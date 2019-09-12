import csv

csvpath = "./budget_data.csv"

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    profit_loss = []
    date = []
    month_change = []   
    
    for row in csvreader:
        profit_loss.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("------------------------------")
    print("Total Months:", len(date))
    print("Total Revenue: $", sum(profit_loss))

    for i in range(1,len(profit_loss)):
        month_change.append(profit_loss[i] - profit_loss[i-1])   
        avg_month_change = sum(month_change)/len(month_change)
        
        max_month_change = max(month_change)

        min_month_change = min(month_change)
        
        max_month_change_date = str(date[month_change.index(max(month_change))])

        min_month_change_date = str(date[month_change.index(min(month_change))])

    print("Avereage Revenue Change: $", round(avg_month_change))
    print("Greatest Increase in Revenue:", max_month_change_date,"($", max_month_change,")")
    print("Greatest Decrease in Revenue:", min_month_change_date,"($", min_month_change,")")