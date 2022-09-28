######################## variable to hold 24 hours * multiply by days input
calculation_to_units = 24
############# string variable to know hours
name_of_unit ="hours"
#######Input variable used at prompt to calculate the hours in the amount of days
user_input = input("Hey user, enter a number of days and I will convert it to hours: ")
#####This function creates a usable input num of days and takes that number * calc_units & adds string hours
def days_to_units(num_of_days):
        return (f"\n{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")

#####This function converts the user input to a integer if a valid numner
#####This function also takes that valid number and checks if it is = 0 or greater than 0
#####The function must be greater than 0 to execute the logic 
def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0, please enter a valid positive number")


    else:
        print("\nYour input is not a valid. Don't ruin my program!")

validate_and_execute()

