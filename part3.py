# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.  
  
# Student ID:               # Date:  28/11/2019
#programming Principles 01 - Part three(Vertical Histogram)
print("*"*51)
print("*"*18, "STAFF VERSION", "*"*18)
print("*"*51)
print("Press any key to start the programme",)
#definig veriables
total=0
progress=" "
progressnum=0
progress_retrailer=" "
progress_retrailernum=0
retrailer=" "
retrailernum=0
exclude=" "
excludenum=0
verticalprogress=""

def credits_checking(a, b, c): #User defined function for checking whether the inputs are within the range
    if (a % 20 != 0 and b % 20 != 0 and c % 20 != 0):
        print("Range error")

def total_checking(a, b, c): #User defined function for checking the total is equal to 120 or not
    if a + b + c != 120:
        print("\nTotal incorrect,The total of the credits must be 120.")

def oneTwenty (a,b,c): #User defined function for checking wether the inputet number is less than or equal to 12o and greater than or equal to 0.

    if a>120 or b>120 or c>120:
        print("Credits should be within the range.(0,20,40,60,80,100,120)")    
    if a<0 or b<0 or c<0:
        print("There can't be any minus values")

def progression(a,b,c): #User defined function for displaying the progression outcome
    global progress,retrailer,exclude,progress_retrailer 
    global progressnum,retrailernum,excludenum,progress_retrailernum,total
    if a==120:
        progress = progress + "*"
        progressnum = progressnum+1
        total = total+1
    elif a==100:
        progress_retrailer = progress_retrailer + "*"
        progress_retrailernum = progress_retrailernum + 1
        total = total + 1
    elif 80<=c<=120:
        exclude = exclude + "*"
        excludenum = excludenum + 1
        total = total + 1
    elif a==0 and 60<=b<=120 and 0<=c<=60:
        retrailer = retrailer + "*"
        retrailernum = retrailernum + 1
        total = total + 1
    elif 20<=a and b==0 and 60<=c<=100:
        retrailer = retrailer + "*"
        retrailernum = retrailernum + 1
        total = total +1
    elif 20<=a<=60 and 40<=b<=100 and c==0:
        retrailer = retrailer + "*"
        retrailernum = retrailernum + 1
        total = total + 1
    elif 20<=a<=100 and 20<=b<=80 and 20<=c<=60:
        retrailer = retrailer + "*"
        retrailernum = retrailernum +1
        total = total + 1
option=""
while option != 'q': #while is used here to loop the programme programme till the user enters the 'q'
    try:
        option=input("Press 'q' to exit the programme and view the histogram.:")
        if option =='q':
            break #if the user enters the 'q' programme break from here go to the ending
        #Getting the inputs passCredits,deferCredits and failCredits
        passCredits = int(input("\nPlease enter your Pass Credits:"))
        deferCredits = int(input("Please enter your Defer Credits:"))
        failCredits = int(input("Please enter your Fail Credits:"))

        credits_checking(passCredits,deferCredits,failCredits) #displaying the number of progressed students and as printed stars
        total_checking(passCredits,deferCredits,failCredits) #Calling the function credits_checking
        oneTwenty(passCredits,deferCredits,failCredits)#Calling the function oneTwenty
        progression(passCredits,deferCredits,failCredits) #Calling the function progression_outcome
    except:
        print("Please enter credits as integers")
        print("_"*50)
print("\nProgress  :",progressnum,progress) #displaying the number of progressed students and as printed stars
print("Trailing  :",progress_retrailernum,progress_retrailer) #displaying the number of trailing students and as printed stars
print("Retriever :",retrailernum,retrailer) #displaying the number of retrieving students and as printed stars
print("Excluded  :",excludenum,exclude) #displaying the number of excluded students and as printed stars
print("\n",total,"outcomes in total.") #displaying the total number of students

vertical= [progressnum,progress_retrailernum,retrailernum,excludenum]
verticalPrinting = max(vertical) #Taking the maximum value from the veriables progressnum,progress_retrailernum,retrailernum and excludenum.

print("\nProgress   Trailing   Retriever   Excluded") #printing the upper part
for x in range(verticalPrinting): #itorating the maximum value from the veriables progressnum,progress_retrailernum,retrailernum and excludenum.
    if progressnum > 0:
        print("   *", end = " ")    
    else:
        print("    ", end = " ")
    progressnum-= 1     
    if progress_retrailernum > 0:
        print("\t       *", end= " ")
    else:
        print("\t        ", end=" ")
    progress_retrailernum-=1
    if retrailernum > 0:
        print("         *", end =" ")    
    else:
        print("          ", end=" ")
    retrailernum-=1    
    if excludenum > 0:
        print("         *")
    else:
        print("          ")
    excludenum -=1    
        
    
    
                 

