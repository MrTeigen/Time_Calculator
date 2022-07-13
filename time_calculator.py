def add_time(start, duration, day = None):

    # Parting different values into different variables for easier handling
    start_time = start.split()[0]
    start_AMPM = start.split()[1]
    start_hour = int(start_time.split(':')[0])
    start_minute = int(start_time.split(':')[1])
    
    added_hour = int(duration.split(':')[0])
    added_minute = int(duration.split(':')[1])
    
    days_passed = 0
    days = {1 : 'Monday', 2 : 'Tuesday', 3 : 'Wednesday', 4 : 'Thursday', 5 : 'Friday', 6 : 'Saturday', 7 : 'Sunday'}
    
    end_AMPM = 'AM'
    
    # Make some easier variable names for handling the resulting minute and hour
    result_minute = start_minute + added_minute
    result_hour = start_hour + added_hour
    
    # Get the day number from days dictionary. PS. REMEMBER THAT THIS INDEX STARTS AT 1
    if day != None:
        for key, value in days.items():
            if day.capitalize() == value:
                start_day = key
    
    # Relocate extra hour and fix the minutes
    if result_minute > 59:
        result_hour += 1
        result_minute -= 60
    
    # Check AM/PM and add 12 hours for easier calculation, revert back later
    if start_AMPM == 'PM':
        result_hour += 12
    
    # Adds the days to a variable and corrects the remaining hours
    if (result_hour >= 25):
        days_passed += (result_hour // 24)
        result_hour = (result_hour % 24)
    
    # Introduces a end_day and checks that it is within the 7 possible weekdays
    if day != None:
        end_day = start_day + days_passed
        while end_day > 7:
            end_day -= 7
    
    # Add a parenthesis with the number of days passed, empty string if none
    if days_passed == 1:
        days_passed = ' (next day)'
    elif days_passed > 1:
        days_passed = ' ({} days later)'.format(days_passed)
    else:
        days_passed = ''
    
    # Checks that the AM / PM formating is correct. If not, corrects it
    if result_hour > 12:
        end_AMPM = 'PM'
        result_hour -= 12
    elif result_hour == 12:
        end_AMPM = 'PM'
    elif result_hour == 0:
        result_hour = 12
    
    
    
    if day != None:
        return '{}:{} {}, {}{}'.format(result_hour, str(result_minute).rjust(2, '0'), end_AMPM, days[end_day], days_passed)
    
    else:
        return '{}:{} {}{}'.format(result_hour, str(result_minute).rjust(2, '0'), end_AMPM , days_passed)
