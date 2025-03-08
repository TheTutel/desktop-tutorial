import time

months = {
    1:"Winter",
    2:"Winter",
    3:"Spring",
    4:"Spring",
    5:"Spring",
    6:"Summer",
    7:"Summer",
    8:"Summer",
    9:"Fall",
    10:"Fall",
    11:"Winter",
    12:"Autummmmia"
}

usname = input("Name:\n")
usmonth = input("Month:")

if usmonth in months:
    print(f'{usmonth.get(months)}')