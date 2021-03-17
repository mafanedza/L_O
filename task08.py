number = 71
def hours(c):
    return str(c//60) + " hour/s and "
def mins(c):
    return str(c%60) + " minutes"
print(hours(number) + mins(number) )