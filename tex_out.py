from print_cal import print_title, print_weekday, print_calender


def print_tex(year, month, firstWeekday, is_month_num=False,
              month_abbreviation=True, weekday_abbreviation=True):
    join = r"&"
    col_head = False
    col_tail = False
    newline = r"\\ \hline"
    newline_in_cell = r""

    title = r"\multicolumn{7}{|c|}{Year Month}\\ \hline \hline"

    weekday_join = r"&"
    weekday_bottom = r"\\ \hline \hline"

    print("""\\begin{table}[htb]\n\centering\n
    \\begin{tabular}{|c|c|c|c|c|c|c|} \\hline""")
    print_title(title, year, month, is_month_num, month_abbreviation)
    print_weekday(firstWeekday, col_head, col_tail, weekday_join,
                  weekday_bottom, newline, weekday_abbreviation)
    print_calender(firstWeekday, year, month, col_head,
                   col_tail, newline, newline_in_cell, join)
    print("\\end{tabular}\n\\end{table}")
