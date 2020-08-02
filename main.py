import calendar
from pukiwiki_out import print_puki
from dokuwiki_out import print_doku
from markdown_out import print_mark
from tex_out import print_tex

year = 2020  # 西暦
month = 8  # 月
firstWeekday = calendar.SUNDAY  # 週のはじめの日
is_month_num = False  # 月を数字表記
is_month_abbreviation = False  # 月を短縮形
is_weekday_abbreviation = True  # 曜日を短縮形


# print calender

print_puki(year, month, firstWeekday, is_month_num,
           is_month_abbreviation, is_weekday_abbreviation)
print_doku(year, month, firstWeekday, is_month_num,
           is_month_abbreviation, is_weekday_abbreviation)
print_mark(year, month, firstWeekday, is_month_num,
           is_month_abbreviation, is_weekday_abbreviation)
print_tex(year, month, firstWeekday, is_month_num,
          is_month_abbreviation, is_weekday_abbreviation)
