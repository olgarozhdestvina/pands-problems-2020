# This program contains a tuple stores the months of the year and
# another tuple from it with just summer months
# and prints out the summer months ine at a time.

month = ("January", 
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December")

summer = month[4:7]
for month in summer:
    print(month)