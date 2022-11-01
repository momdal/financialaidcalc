#Name: Megan Omdal
#Date: 09-30-2022
#Description: This program prompts the user to enter their first name,
#             last name, annual salary, family size and Veteran status
#             to determine financial aid eligibility and print the results.
#             In order to be eligible, the user must either have less
#             than $15,000 annual salary and a family of 3 or more, or they
#             must be a Veteran.
#
######################################################################################################################################################################################################
#
#
#Declarations:
firstName = 0
lastName = 0
annualSalary = 0
familySize = 0
vetStatus = 0

#Input
#The user is asked to input their first and last name, annual salary, family size, and Veteran status.
firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
annualSalary = int(input("Enter your annual salary: "))
familySize = int(input("Enter your family size: "))
vetStatus = int(input("Are you a Veteran? Please enter 1 for yes and 2 for no: "))

#Calculations and Output
# The else if statements decide if the input provided by the user meets the qualifications for eligibility
# Output prints the input and eligiblity results
if annualSalary > 15000 and familySize < 3 and vetStatus == 2:
    print("You have entered " + firstName + " " + lastName + " " + str(annualSalary) + " " + str(familySize) + " " + str(vetStatus) + " and unfortunately you do not qualify for financial aid.")
elif annualSalary > 15000 and familySize >= 3 and vetStatus == 2:
        print("You have entered " + firstName + " " + lastName + " " + str(annualSalary) + " " + str(familySize) + " " + str(vetStatus) + " and unfortunately you do not qualify for financial aid.")
elif annualSalary < 15000 and familySize < 3 and vetStatus == 2:
        print("You have entered " + firstName + " " + lastName + " " + str(annualSalary) + " " + str(familySize) + " " + str(vetStatus) + " and unfortunately you do not qualify for financial aid.")
elif annualSalary < 15000 and familySize >= 3 and vetStatus == 2:
        print("You have entered " + firstName + " " + lastName + " " + str(annualSalary) + " " + str(familySize) + " " + str(vetStatus) + " Congrats! You do qualify for financial aid!")
elif annualSalary > 15000 and familySize < 3 and vetStatus == 1:
        print("You have entered " + firstName + " " + lastName + " " + str(annualSalary) + " " + str(familySize) + " " + str(vetStatus) + " Congrats! You do qualify for financial aid!")
elif annualSalary > 15000 and familySize >= 3 and vetStatus == 1:
        print("You have entered " + firstName + " " + lastName + " " + str(annualSalary) + " " + str(familySize) + " " + str(vetStatus) + " Congrats! You do qualify for financial aid!")
elif annualSalary < 15000 and familySize < 3 and vetStatus == 1:
        print("You have entered " + firstName + " " + lastName + " " + str(annualSalary) + " " + str(familySize) + " " + str(vetStatus) + " Congrats! You do qualify for financial aid!")
elif annualSalary < 15000 and familySize >= 3 and vetStatus == 1:
        print("You have entered " + firstName + " " + lastName + " " + str(annualSalary) + " " + str(familySize) + " " + str(vetStatus) + " Congrats! You do qualify for financial aid!")


#######################################################################################################################################################################################################
