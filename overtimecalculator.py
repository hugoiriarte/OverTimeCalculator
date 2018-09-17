"""
Program: overtimecalculator.py
Arthur: Hugo
Program that computes weekly pay with over time
"""

#User Input
hourlyWage = float(input("what is your hourly wage >>"))
hoursWorked = float(input("How many hours did you work this week >>"))
overTimeWorked = float(input("How many hours of overtime did you do this week >>"))

#Constant
OVER_TIME = 1.5 * hourlyWage

#Computation
totalWeekPay = float(hourlyWage * hoursWorked + (overTimeWorked * OVER_TIME))

#Results
print("Your weekly pay is $" + str(totalWeekPay) + "0")