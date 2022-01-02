''' Welcome to Expense Calculator
Problem: I wanted to keep track of my basic expenses in a quick and easy way without having to make a spreedsheet
everytime. I also wanted something that would clearly show me how much more time I would need to work in order
to save up for an item(ex.car). Lastly, like a spreadsheet I wanted my data to be saved in a format I could access
at another time. 
'''

#  -----Global Variables-----
end = True
expenseSum = 0.0
incomeSum = 0.0
expenseComplete = False
incomeComplete = False


# -----Functions----- 

def spendingCalculator(expenses): 
        global expenseSum          # for python to understand its global variable
        list = expenses.split(",") 
        for numbers in list: 
           expenseSum += float(numbers) # increments so that users can go back and add more
        return round(expenseSum, 2) # rounds to 2 decimal places 

def incomeCalculator(wage, hours): 
        global incomeSum            # for python to understand its global variable
        incomeSum += wage * hours   # increments so that users can go back and add more
        return round(incomeSum, 2)

def savingRateCalculator(typeofTime, timeTaken, moneySaved, moneyGoal): 
        moneyPerTime = moneySaved/timeTaken
        totalTime = moneyGoal/moneyPerTime
        return "it will take about " + str(round(totalTime, 1)) + " " + typeofTime.lower() + " to reach your saving goal"

def viewStatement(incomeSum, expenseSum):  
            if expenseSum > incomeSum:          # checks which is bigger to determine what to subtract with what
                return"You are over spending by $" + str(round(expenseSum - incomeSum), 2 )
            else: 
                return"You are saving $" + str(round((incomeSum - expenseSum), 2))



#  ------Main program UI (loops till user exits so that they can add up their data) :-----

while end: 
    # Main Menu
    print()
    print("Enter the number for an option below:")
    print("1.Add spending\n2.Add income\n3.View Statement\n4.Saving Goal Calculator\n5.Export\n6.Exit")
    print()

    #Takes input of user's choice
    n = input()

    # Spending calculator that sums up spending
    if "1" in n: 
        s = input("Enter the money amounts you have spent seperated by commas(ex. 24, 12, 92): ")
        print("Your spending totals to: $", spendingCalculator(s))
        expenseComplete = True # lets program know that expense process was completed

    # Income Calculator
    elif "2" in n: 
        w = float(input("What is your hourly wage? $"))
        h = float(input("How many hours have you worked? "))
        print("Your income totals to: $", incomeCalculator(w, h))
        incomeComplete = True # Lets program know that income process was completed

    
    # Calculating overall money saved or lost
    elif "3" in n: 
        if expenseComplete and incomeComplete:
            print(viewStatement(incomeSum, expenseSum))
        else: 
            print("ERROR: make sure to add both income and expense to access this") 
    
    # For calculating the time needed to make a sum of money according to current saving rate
    elif "4" in n: 
        moneyGoal = float(input("How much money do you want to save up for what you want? $"))
        moneySaved = float(input("How much money have you saved up so far(must be greater than $0)? $"))
        timeTaken =  float(input("How long did it take to save this amount?(units asked next) "))
        typeofTime = input("What unit of time is this? ")
        print(savingRateCalculator(typeofTime, timeTaken, moneySaved, moneyGoal))

    # exports all the data to a text file(it can also add data to exisitng text files so users don't have too many files)
    elif "5" in n: 
        if expenseComplete and incomeComplete:
            date = input("Please enter time period(ex. Feb21,2020 to Mar21,2020): ")
            name = input("What would you like to call the file(If one exists enter the same name)? ")
            name += ".txt"
            f = open(name, "a")     # allows it to append to a old file if it exists or create a new one
            f.write("\nExported from Expense Calculator:\n\n")
            f.write(date  + " \n")
            f.write("\tYour expense total was: $" + str(expenseSum)  + "\n"
            + "\tYour income total was: $" +  str(incomeSum) + "\n"
            + "\tYour Statement is: " + str(viewStatement(incomeSum, expenseSum)) + "\n")
            f.close() 
            # After exporting all values reset so if calculating for a different period it doesn't add from previous
            expenseSum = 0
            incomeSum = 0
            expenseComplete = False
            incomeComplete = False
        else: # incase income and expense hasn't been filled out
             print("ERROR: make sure to add both income and expense to access")
            

    #for exiting the loop 
    elif "6" in n: 
        end = False

    # incase user makes a typo
    else: 
        print("Error please read instructions and try again!")

    # so that users can clearly read their output before continuing to main menu once again
    if "1" in n or "2" in n or "3" in n or "4" in n or "5" in n: # So press to continue doesn't appear for exiting the code 
        n = input("Press Enter to continue!")