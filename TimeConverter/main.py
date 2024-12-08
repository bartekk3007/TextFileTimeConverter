
def convert_time(timeString):
    timePart = timeString.split(':')
    firstPart = int(timePart[0])*60
    secondPart = float(timePart[1])
    timeNumber = firstPart + secondPart
    roundNumber = round(timeNumber, 3)
    return roundNumber

f = open("CornersTimes.txt", "r")
outputFile = open('TimesSeconds.txt', 'w')
for line in f:
    values = line.split("\t")
    time_converted = convert_time(values[1])
    print(time_converted)
    outputFile.write(str(time_converted) + "\n")