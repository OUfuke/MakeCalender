import calendar


def print_title(title, year, month, is_month_num, month_abbreviation):
    title = title.replace("Year", str(year))
    if is_month_num:
        title = title.replace("Month", str(month))
    else:
        if month_abbreviation:
            title = title.replace("Month", calendar.month_abbr[month])
        else:
            title = title.replace("Month", calendar.month_name[month])
    print(title)


def print_weekday(firstWeekday, col_head, col_tail, weekday_join,
                  weekday_bottom, newline, weekday_abbreviation):
    for day in range(7):
        if day == 0:
            if col_head:
                print(weekday_join, end="  ")
        else:
            print(weekday_join, end="  ")
        day_tmp = (day + firstWeekday) % 7
        if weekday_abbreviation:
            print(calendar.day_abbr[day_tmp], end="  ")
        else:
            print(calendar.day_name[day_tmp], end="  ")
    if col_tail:
        print(weekday_join, end="")
    if weekday_bottom == "":
        print(newline)
    else:
        print(weekday_bottom)


def print_calender(firstWeekday, year, month, col_head, col_tail, newline,
                   newline_in_cell, join):
    calendar.setfirstweekday(firstWeekday)
    out_calendar = calendar.monthcalendar(year, month)
    for week in out_calendar:
        for num, day in enumerate(week):
            if num == 0:
                if col_head:
                    print(join, end="  ")
            else:
                print(join, end="  ")
            if day != 0:
                print(str(day) + newline_in_cell, end="  ")
        if col_tail:
            print(join, end="")
        print(newline)
