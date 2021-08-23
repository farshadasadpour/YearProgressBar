import datetime

today = datetime.date.today()
start_year = datetime.date(2020, 1, 1)
end_year = datetime.date(2020, 12, 30)
passed_days = (today - start_year).days
remaining_days = (end_year - today).days
# print(passed_days,remaining_days,passed_days+remaining_days)
passed_days_char = '█'
remaining_days_char = '░'
passed_days_progressbar=(passed_days_char * int(passed_days / 15))
remaining_days_progressbar=(remaining_days_char * int(remaining_days / 15))
calc_Percent_passed_days=(passed_days/(passed_days+remaining_days)*100)
calc_Percent_remaining_days=(remaining_days/(passed_days+remaining_days)*100)

print('%.2f%s %s%s %.2f%s'%(calc_Percent_passed_days,'%',passed_days_progressbar,remaining_days_progressbar,calc_Percent_remaining_days,'%'))