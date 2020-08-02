from print_cal import print_title, print_weekday, print_calender


def print_puki(year, month, firstWeekday, is_month_num=False,
               month_abbreviation=True, weekday_abbreviation=True):
    join = r"|"
    col_head = True
    col_tail = True
    newline = r""
    newline_in_cell = r"&br;"

    title = r"|>|>|>|>|>|>| Year Month |h"

    weekday_join = r"|"
    weekday_bottom = r"h"

    print("|CENTER:" * 7 + "|c")
    print_title(title, year, month, is_month_num, month_abbreviation)
    print_weekday(firstWeekday, col_head, col_tail, weekday_join,
                  weekday_bottom, newline, weekday_abbreviation)
    print_calender(firstWeekday, year, month, col_head,
                   col_tail, newline, newline_in_cell, join)
