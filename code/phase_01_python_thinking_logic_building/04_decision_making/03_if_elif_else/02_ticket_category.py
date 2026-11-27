"""
Topic: if elif else

Problem:
Select ticket category based on age.

Logic:
Below 5  : Free
5-18     : Child Ticket
19-60    : Adult Ticket
Above 60 : Senior Citizen Ticket
"""


age = 25


if age < 5:
    print("Free Ticket")

elif age <= 18:
    print("Child Ticket")

elif age <= 60:
    print("Adult Ticket")

else:
    print("Senior Citizen Ticket")