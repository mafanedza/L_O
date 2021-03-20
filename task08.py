def hours(c):
    if c//60 < 2:
      return str(c//60) + " hour, " + str(c%60) + " minutes"
    else:
        return str(c//60) + " hours, " + str(c%60) + " minutes"
print(hours(126))
