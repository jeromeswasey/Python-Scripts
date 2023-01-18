######A program used to calculate the number of hours in the input(num_of_days). The program also validates the input logic to make sure it is within the rules of a positive number and not any other valid than a valid day input. The program will print the number of hours and the days entered or will print invalid if the answer is not a relevant value.
######################## variable to hold 365 days * multiply by years input
calculation_to_units = 365
############# string variable to know days in a year
name_of_unit ="days"

#####This function creates a usable input num of years and takes that number * calc_units (365) & adds string days
def years_to_days(num_of_years):
        return (f"\n{num_of_years} years are {num_of_years * calculation_to_units} {name_of_unit}")

#####This function converts the user input to a integer if a valid number
#####This function also takes that valid number and checks if it is = 0 or greater than 0
#####The function must be greater than 0 to execute the logic 
def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = years_to_days(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0, please enter a valid positive number")


    else:
        print("\nYour input is not a valid. Don't ruin my program!")
###############Defines user input variable for the while loop to pull from
user_input = ""
################Continues loop until the user enters "exit"
while user_input != "exit":
    #######Input variable used at prompt to calculate the days in the amount of years
    user_input = input("Hey user, enter a number of years and I will convert it to the amount of days in the year amount: ")
    validate_and_execute()

