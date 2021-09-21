seconds_start = int(input('Please enter amount of seconds: '))
days = seconds_start // (24 * 60 * 60)
hours = (seconds_start % (24 * 60 * 60)) // (60 * 60)
minutes = ((seconds_start % (24 * 60 * 60)) % (60 * 60)) // (60)
seconds = seconds_start % (24 * 60 * 60)
print(days, ':' , hours, ':' , minutes, ':' , seconds)
seconds %= 24 * 60 * 60