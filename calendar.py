import calendar
# we hold meeting every first monday at of the month.

for month in range(1, 13):
   mycal = calendar.monthcalendar(2025, month)
   week1 = mycal[0]
   week2 = mycal[1]

   if week1[calendar.MONDAY] != 0:
       auditday = week1[calendar.MONDAY]
   else:
       auditday = week2[calendar.MONDAY]

   print("%10s %2d" % (calendar.month_name[month], auditday))
