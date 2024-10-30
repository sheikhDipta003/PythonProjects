import calendar

y = int(input("Enter a year: "))
m = int(input("Enter a month: "))
x = calendar.month(y, m)
print(type(x))
print(calendar.month(y, m))
