# Olga Rozhdestvina
# The program that outputs whether or not today is a weekday. 

from datetime import datetime

today = datetime.today()

if today.weekday() <= 4:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")