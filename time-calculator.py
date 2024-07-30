def add_time(start, duration, day_name = ''):
    # time given
    colon_index = start.find(':')
    hours = int(start[0:colon_index])
    mins = int(start[colon_index + 1: colon_index + 3])
    day_time = start[-2:]
    if day_time == 'PM':
        # converting in 24hr format
        hours = 12 + hours
    curr_time = (hours * 60) + mins
    print('Given time: ' , curr_time)

    # time to be added
    hours_to_add = int(duration[0:duration.find(':')])
    mins_to_add = int(duration[duration.find(':') + 1:])
    time_to_add = (hours_to_add * 60) + mins_to_add
    print('Time to Add: ', time_to_add)

    # new time
    new_time = curr_time + time_to_add
    days = (new_time // 1440) # get no. of days
    new_time = new_time % 1440  # get time of day
    new_time_hrs = new_time // 60
    new_time_mins = new_time % 60
    time_str = ('12' if new_time_hrs % 12 == 0 else str(new_time_hrs % 12)) + ':' + ('0' + str(new_time_mins) if len(str(new_time_mins)) == 1 else str(new_time_mins))
    time_str += ' PM' if new_time_hrs >= 12 else ' AM'
    if day_name:
        day_name = day_name.lower()
        print(day_name)
        week_days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        day_index = week_days.index(day_name) + days
        new_day = week_days[day_index % 7]
        print(new_day)
        time_str += ', ' + new_day[0].upper() + new_day[1:]
    if days:
        time_str += ' (next day)' if days == 1 else f' ({days} days later)'
    print(time_str)
    return time_str

add_time('3:30 PM', '2:12')
