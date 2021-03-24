def hours(c):
    if c//60 < 2 and c%60 >=2:
      return str(c//60) + " hour, " + str(c%60) + " minutes"
    elif c%60 >= 2 and c//60 >=2:
        return str(c//60) + " hours, " + str(c%60) + " minutes"
    elif c//60 < 2 and c%60 < 2:
        return str(c//60) + " hour, " + str(c%60) + " minute"
    elif c//60 >= 2 and c%60 < 2:
        return str(c//60) + " hours, " + str(c%60) + " minute"
print(hours(133))
