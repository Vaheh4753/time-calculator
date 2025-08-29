def add_time(start, duration, starting_day=''):
    
    # Extracting needed variables from parameters
    split_start = start.split(':')
    start_hours = int(split_start[0])
    split_start_no_hours = split_start[1].split(' ')
    start_minutes = int(split_start_no_hours[0])
    am_or_pm_start =  split_start_no_hours[1]
    duration_split = duration.split(':')
    duration_hours = int(duration_split[0])
    duration_minutes = int(duration_split[1])
    starting_day = starting_day.lower()
    
    # Dict for days of the week
    days = {
        'monday': 1,
        'tuesday': 2,
        'wednesday': 3,
        'thursday': 4,
        'friday': 5,
        'saturday': 6,
        'sunday': 0
        }
    
    # Finding total days later
    if am_or_pm_start.upper() == 'PM':
        start_hours += 12
    if start_minutes + duration_minutes > 60:
        start_hours += 1
    days_elapsed = int((start_hours + duration_hours +(start_minutes + duration_minutes)/60)//24)
    time_24_format = (start_hours + duration_hours) % 24
    time_final_minutes = (start_minutes + duration_minutes) % 60
    
    # Finding hours for end time and AM or PM 
    if time_24_format == 12:
        time_final_hours = time_24_format
        am_or_pm_end = 'PM'
    elif time_24_format > 12:
        time_final_hours = time_24_format - 12
        am_or_pm_end = 'PM'
    else:
        if time_24_format == 0:
            time_final_hours = time_24_format + 12
        else:
            time_final_hours = time_24_format
        am_or_pm_end = 'AM'
    end_day = ''
    
    # day_key is the value for the ending day
    if starting_day != '':
        for key, value in days.items():
            if value == (days[starting_day] + days_elapsed) % 7:
                end_day = ', ' + key.capitalize()
    
    # Combining final hours and final minutes into clock format
    end_time = str(time_final_hours) + ':' + (str(time_final_minutes) if time_final_minutes > 9 else '0' + str(time_final_minutes))
    
    # Producing output string
    if days_elapsed >= 2:
        final_string = end_time + ' ' + am_or_pm_end + end_day + ' (' + str(days_elapsed) + ' days later)'
    elif days_elapsed == 1:
        if end_day == '':
            final_string = end_time + ' ' + am_or_pm_end + ' (next day)'
        else:
            final_string = end_time + ' ' + am_or_pm_end + end_day + ' (next day)'
    elif days_elapsed == 0:
        final_string = end_time + ' ' + am_or_pm_end + end_day
    print(final_string)

def main():
    add_time('3:00 PM', '12:00', 'tuesday')
    return
main()
