date=int(input("Enter the date "))
month=int(input("Enter the month "))
year=int(input("Enter the year "))
if(date<31 and month<12):
  print("Date= ", date+1, "Months= ", month, "Year= ", year)
elif(date==31 and month==12):
  date=1
  month=1
  year=year+1
  print("Date= ", date, "Months= ", month, "Year= ", year)
else:
  print("Invalid date")