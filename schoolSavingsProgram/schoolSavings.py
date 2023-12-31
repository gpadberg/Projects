# Student name: Grace Padberg 
# Assignment completed as part of ENCMP 100, a class at 
# the University of Alberta, Department of Electrical and Computer Engineering

# Program aimed to determine whether a student had saved enough to cover tuition for a specific program
# Program needs added functionality for user-entered savings. 
import matplotlib.pyplot as plt
import numpy as np

# Interest Rate Setting: 
defaultInterestRate = int(input("Please enter 1 if you would like to enter your own interest rate or 2 to use the default rate: "))
if defaultInterestRate == 1:
    monthlyinterestrate = float(input("Enter your interest rate here: "))
else: 
    monthlyinterestrate = 0.005208333333333333333

# Monthly Contribution Setting: 
monthlycontribution = int(input("Please enter the amount you intend to contribute montly, in dollars: "))

# Lump Sum Setting:
initialLumpSum = int(input("Please enter the lump sum you plan to invest at the present day: "))
save = [initialLumpSum]
for i in range(0,215):
    save = save + [save[i] + save[i]*monthlyinterestrate + monthlycontribution]
print("The savings amount is $%.2f" %save[215])



# TUITION CALCULATION
# calculates the increase in tuition over 22 years for three different programs,
# adds the last 4 years for each program to give the projected total tuition cost. 
tuitionincrease = 1.07 
artscost = [5550]
for i in range (0,22): 
    artscost = artscost + [artscost[i]*tuitionincrease]
artssum = sum(artscost[18:22])
print("The cost of the arts program is $%.2f" %artssum)
artx = [artssum]*216

    
sciencecost = [6150]
for i in range (0,21): 
    sciencecost = sciencecost + [sciencecost[i]*tuitionincrease]
sciencesum = sum(sciencecost[18:22])
print("The cost of the science program is $%.2f" %sciencesum)
sciencex = [sciencesum]*216
    

engcost = [6550]
for i in range (0,21): 
    engcost = engcost + [engcost[i]*tuitionincrease]
engsum = sum(engcost[18:22])
print("The cost of the engg program is $%.2f" %engsum)
engx = [engsum]*216


# PLOT
# plots the saving balance, and each of the costs for tuition, scaling back the 
# years to 18, adding labels, a legend, and specific increments for the x-axis. 

# PLOT
# plots the saving balance, and each of the costs for tuition, scaling back the 
# years to 18, adding labels, a legend, and specific increments for the x-axis. 
plt.xlabel("Years")
plt.ylabel('Amount ($)')
plt.title('Savings vs Tuition')
plt.plot(np.arange(0,18,1/12),save, label = "Saving Balance")
plt.plot(np.arange(0,18,1/12),artx, label = "Arts")
plt.plot(np.arange(0,18,1/12),sciencex, label = "Science")
plt.plot(np.arange(0,18,1/12),engx, label = "Engineering")
plt.xlim([0,18])
plt.ylim([0,100000])
plt.xticks(range(0,19))
plt.xlabel("Years")
plt.ylabel('Amount ($)')
plt.title('Savings vs Tuition')
plt.legend()
plt.show()


# Optimization
# This section allows the user to input a number in order to choose the program
# they want to evaluate for. It then checks whether the user has enough saved 
# to cover the program cost. The program then computes what the optimal monthly
# contribution is based on a $1 increase per month. 
choice = int(input('Enter a program (1) - Arts, (2) - Science, (3) - Engineering: '))
month = 0
match choice:
    case 1: 
        targAmt = artssum # arts
        programname = 'arts'
    case 2:
        targAmt = sciencesum # science
        programname = 'science'
    case 3:
        targAmt = engsum # engineering
        programname = 'engineering'
        
if save[215] < targAmt:
    print('Unfortunately you do not have enough saved for the',programname,'program')
else:
    print('Congratulations! You have saved enough for the',programname,'program')
save = [2000]
while save[-1] < targAmt:
   month = month + 1
   save = [2000]
   for i in range(0,215):
      save = save + [save[i] + save[i]*monthlyinterestrate + month]
print('The optimal monthly contribution amount is $%.0f' %month)