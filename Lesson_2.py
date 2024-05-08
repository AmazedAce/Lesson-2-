Task 1: Code Correction 

number = float(input("Enter a number: ")) 

 if number > 0: 

    print("The number is positive.") 

elif number == 0: 

    print("The number is zero.") 

else: 

    print("The number is negative.") 

 



2. The Greatest Showdown 

Objective: 
Harness the power of conditional statements to compare and determine values. 

Task 1: Identify the Greatest 

num1 = float(input("Enter the first number: ")) 

num2 = float(input("Enter the second number: ")) 

num3 = float(input("Enter the third number: ")) 

  

 greatest = max(num1, num2, num3) 

  

 print("The greatest number is:", greatest) 

 

 

 

Task 2: Identify the Smallest 
Extend your program from Task 1 to also 
determine the smallest number among the three and print it out. 

 

num1 = float(input("Enter the first number: ")) 

num2 = float(input("Enter the second number: ")) 

num3 = float(input("Enter the third number: ")) 

  

smallest = min(num1, num2, num3) 

  

print("The smallest number is:", smallest) 

 

 


Task 3: Equality Check 
Enhance your program to handle cases where two or all of the numbers are equal. 
The program should display appropriate messages like 
"Two numbers are equal and the largest" or "All numbers are equal". 

 

 

num1 = float(input("Enter the first number: ")) 

num2 = float(input("Enter the second number: ")) 

num3 = float(input("Enter the third number: ")) 

   

smallest = min(num1, num2, num3) 

largest = max(num1, num2, num3) 

      

if num1 == num2 == num3: 

    print(f"All numbers are equal. The smallest and largest number is {smallest}.") 

else: 

    messages = [] 

    if num1 == num2: 

        messages.append(f"{num1} and {num2} are equal") 

    if num1 == num3: 

        messages.append(f"{num1} and {num3} are equal") 

    if num2 == num3: 

        messages.append(f"{num2} and {num3} are equal") 

  

   

    equality_msg = ". ".join(messages) + "." if messages else "" 

    print(f"The smallest number is {smallest}. The largest number is {largest}. {equality_msg}") 

 

3. Leap Year Explorer 

Objective: 
Dive deep into the intricacies of the calendar by exploring the concept of leap years. 

 

def check_leap_year(): 

    year = int(input("Enter a year: ")) 


    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0): 

        print(f"The year {year} is a leap year.") 

    else: 

        print(f"The year {year} is not a leap year.") 

check_leap_year() 