
# Calculating the net monthly income of the employee after the tax is deducted:

#CONSTANTS:   
FIXED_INCOME_TAX = 18 # Percentage %
CHEF_HOURLY_RATE = 30
WAITER_HOURLY_RATE = 28
DELIVERY_HOURLY_RATE = 25
CLEANER_HOURLY_RATE = 24


        
# VARIABLES:
employee_position = ""
employee_monthly_hours = 0


# METHODS DEFINITION:
    
def validate_employee_position_and_calculate(employee_position, employee_monthly_hours, new_paramter):

    if employee_position.lower() == 'chef':             
        result = calculate_net_monthly_employee_income(CHEF_HOURLY_RATE, employee_monthly_hours)       
        print(str(employee_position.upper()) + "\n" 
            "Net monthly income:" + str(result))
        
    elif employee_position.lower() == 'waiter':       
        result = calculate_net_monthly_employee_income(WAITER_HOURLY_RATE, employee_monthly_hours)    
        print(str(employee_position.upper()) + "\n" 
            "Net monthly income:" + str(results))
        
    elif employee_position.lower() == 'delivery':       
        result = calculate_net_monthly_employee_income(DELIVERY_HOURLY_RATE, employee_monthly_hours)           
        print(str(employee_position.upper()) + "\n" 
            "Net monthly income:" + str(result))  
                
    elif employee_position.lower() == 'cleaner':     
        result = calculate_net_monthly_employee_income(CLEANER_HOURLY_RATE, employee_monthly_hours)   
        print(str(employee_position.upper()) + "\n" 
            "Net monthly income:" + str(result))
        
    else:
        print("Invalid input. please enter only an employee position from the list")
         

         
def calculate_net_monthly_employee_income(hourly_rate, employee_monthly_hours):   
    gross_income = employee_monthly_hours * hourly_rate
    tax_deducted = gross_income * FIXED_INCOME_TAX / 100
    net_monthly_employee_income = gross_income - tax_deducted  
    
    return net_monthly_employee_income
    
             

# USER INPUT:
employee_position = input("Enter the position of employee : chef | waiter | delivery | cleaner :")
employee_monthly_hours_float = float(input("Enter the number of monthly hours the employee worked: Don't use commas "))  
employee_monthly_hours = int(round(employee_monthly_hours_float))

 

# Method Execution:
validate_employee_position_and_calculate(employee_position, employee_monthly_hours)


