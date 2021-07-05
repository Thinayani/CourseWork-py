# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.  
  
# Student ID:                # Date:  28/11/2019
#programming Principles 01 - Part one(Student Version) change
print("")
print("*" * 50)
header="Calculate your Progression Outcome"
center=header.center(50)
print(center)
print("*"*16,"STUDENT  VERSION","*"*16)
print("*" * 50)


def credits_checking(a, b, c): #User defined function for checking whether the inputs are within the range
    if (a % 20 != 0 or b % 20 != 0 or c % 20 != 0):
        print("Range error")


def total_checking(a, b, c): #User defined function for checking the total is equal to 120 or not
    if a + b + c != 120:
        print("\nTotal incorrect")

def oneTwenty (a,b,c): #User defined function for checking wether the inputet number is less than or equal to 12o and greater than or equal to 0.
    if a>120 or b>120 or c>120:
        print("Credits should be within the range.(0,20,40,60,80,100,120)")    
    if a<0 or b<0 or c<0:
        print("There can't be any - values")

#Making changes to the file        

def progression_outcome(a, b, c): #User defined function for displaying the progression outcome
    if a == 120:
        print("\nProgress")
    elif a == 100:
        print("\nProgress - module retrailer")
    elif a <= 40 and b <= 40 and c >= 80:
        print("\nExclude")
    elif a==0 and 60<=b<=120 and 0<=c<=60:
        print("\nDo not progress - module trailer")
    elif 20<=a and b==0 and 60<=c<=100:
        print("\nDo not progress - module retrailer")
    elif 20<=a<=60 and 40<=b<=100 and c==0:
        print("\nDo not progress - module retrailer")
    elif 20<=a<=100 and 20<=b<=80 and 20<=c<=60:
        print("\nDo not progress - module retrailer")
    else:
        print("")
 
while True: #error handling through try and except
    try: #Programme starts here. #Getting the inputs passCredits,deferCredits and failCredits
        passCredits = int(input("\nPlease enter your Pass Credits:"))
        deferCredits = int(input("Please enter your Defer Credits:"))
        failCredits = int(input("Please enter your Fail Credits:"))

        oneTwenty(passCredits, deferCredits, failCredits) #Calling the function oneTwenty
        
        credits_checking(passCredits, deferCredits, failCredits) #Calling the function credits_checking

        total_checking(passCredits, deferCredits, failCredits) #Calling the function total_checking

        progression_outcome(passCredits, deferCredits, failCredits) #Calling the function progression_outcome
        break
    except ValueError:
        print("\nIntegers required")#error handling through try and except

print("\nProgramme is now exiting...")
print("_"*50)
