#Question 4
#In the tutorial, you defined several variables to calculate the total number of seconds in a year. Run the next code cell to do the calculation here.

# Create variables
num_years = 4
days_per_year = 365 
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

# Calculate number of seconds in four years
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)



# TODO: Set the value of the births_per_min variable
births_per_min = 250

# TODO: Set the value of the births_per_day variable
births_per_day = hours_per_day * mins_per_hour * births_per_min