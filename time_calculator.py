def add_time(start, duration,day = None):
    #Starting variables
    list_of_days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    week_length = len(list_of_days)
    max_hour = 12
    max_minute = 59

    #Separate the strings into organized pieces
    #Initial separation of number from am or pm
    split_start_am_pm = start.split()[0]
    #am or pm stored in a variable
    am_pm = start.split()[1]
    #store start time into variable
    sep_start_time = split_start_am_pm.split(":")
    #Store time to add into variable
    split_add_time = duration.split(":")
    #add minutes part of each time variable
    add_min = int(sep_start_time[1]) + int(split_add_time[1])
    #Make sure hour time is an int
    split_add_time[0] = int(split_add_time[0])


    #Check if minute is over the max add the extra to the hour
    if add_min > max_minute:
        split_add_time[0] += 1
        add_min = add_min - 60
    
    #add hours together of start time and added time
    add_hour = int(sep_start_time[0]) + int(split_add_time[0])
    
    #Variables for days and time PM or AM 
    am_pm_change = 0
    day_change = 0

    #Logic to figure out how many am and pm changes happened to lay foundation for the day conversion
    if add_hour > max_hour:
        while add_hour > max_hour:
            am_pm_change += 1
            add_hour = add_hour - max_hour

    #Add 0 to beginning of minutes if less than 10
    if add_min < 10:
        add_min = "0" + str(add_min)

    #Logic to figure out AM or PM
    if am_pm_change % 2 == 1:
        if am_pm == "PM":
            am_pm = "AM"
            am_pm_change += 1
        else:
            am_pm = "PM"
    else:
        am_pm = am_pm

    #Convert am and pm changes to how many days have passed
    day_change = round(am_pm_change/2)

    #Change am and pm if hour lands on the 12
    if add_hour == max_hour:
        if am_pm == "PM":
            am_pm = "AM"
            day_change += 1
        else:
            am_pm = "PM"
    
    #Logic to figure out what day of the week to print or none at all
    if day != None:
        end_day = 0
        start_day =  day.title()
        if start_day in list_of_days:
            day_1 = list_of_days.index(start_day)
            end_day = int(day_1) + int(day_change)
            while end_day >= week_length:
                end_day = end_day - week_length
            day = list_of_days[end_day]
    else:
        day = None
        

    #Logic to find the amount of days that pass from the added time
    duration_text = ""
    if day_change == 1:
        duration_text = " (next day)"
    elif day_change > 1 :
        duration_text = " (" +  str(day_change) + " days later)"

    #What is returned from this function
    if day != None:
        return( str(add_hour) + ":" + str(add_min) + " "+am_pm + ", "+ day + duration_text)
    else:
        return( str(add_hour) + ":" + str(add_min) + " "+am_pm + duration_text)