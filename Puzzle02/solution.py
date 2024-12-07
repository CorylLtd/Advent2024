def areNumbersSafe(numbers):
    # are they all incrementing by 1 - 3?
    allIncrementing = True
    for i in range(len(numbers) - 1):
        if int(numbers[i]) - int(numbers[i + 1]) < -3 or int(numbers[i]) - int(numbers[i + 1]) >= 0:
            allIncrementing = False
            break

    allDecrementing = True
    for i in range(len(numbers) - 1):
        if int(numbers[i]) - int(numbers[i + 1]) > 3 or int(numbers[i]) - int(numbers[i + 1]) <= 0:
            allDecrementing = False
            break

    return allIncrementing or allDecrementing

def isSafe(line):
    # split the line into a list of integers
    data = line.split(' ')
    if (areNumbersSafe(data)):
        return True

    # try removing each number and see if the list is safe
    for i in range(len(data)):
        newNumbers = data[0:i] + data[i+1:]
        if (areNumbersSafe(newNumbers)):
            return True
    return False

safeCount = 0
# load the data
with open('input.txt') as f:
    for line in f:
        if isSafe(line):
            safeCount += 1
print('Safe count', safeCount)